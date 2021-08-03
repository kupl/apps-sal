s = input()
n = len(s)

res1 = 0
res2 = 0

for i in range(n):
    if i % 2 == 0:
        if s[i] == "0":
            res1 += 1
        else:
            res2 += 1
    else:
        if s[i] == "1":
            res1 += 1
        else:
            res2 += 1

print(min(res1, res2))
