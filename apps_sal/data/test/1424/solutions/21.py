def dif(a, b):
    (b, a, ans) = (max(a, b), min(a, b), 0)
    (c, d) = ([], [])
    i = 0
    while a > 0:
        if a % 2 == 1:
            c.append(1)
        else:
            c.append(0)
        a //= 2
        i += 1
    i = 0
    while b > 0:
        if b % 2 == 1:
            d.append(1)
        else:
            d.append(0)
        b //= 2
    for i in range(len(c)):
        if c[i] != d[i]:
            ans += 1
    for i in range(len(c), len(d)):
        if d[i] == 1:
            ans += 1
    return ans


(n, m, k) = map(int, input().split())
ans = 0
x = []
for i in range(m + 1):
    x.append(int(input()))
for i in range(m):
    if dif(x[i], x[m]) <= k:
        ans += 1
print(ans)
