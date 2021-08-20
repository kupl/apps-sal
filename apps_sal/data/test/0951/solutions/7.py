k = int(input())
n = list(map(int, sorted(input())))
s = sum(n)
idx = 0
res = 0
while k > s:
    s += 9 - n[idx]
    res += 1
    idx += 1
print(res)
