n = input()
m = int(input())
res = 0
pw = 1
for i in range(len(n) - 1, -1, -1):
    res = (res + pw * int(n[i])) % m
    if i > 0:
        pw = pw * 10 % m
partial = res
for x in n:
    if int(x) != 0:
        res = min(res, partial)
    partial = (partial - int(x) * pw) % m
    partial = (partial * 10 + int(x)) % m
print(res)
