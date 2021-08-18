n, m, x = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]
ans = []
for i in range(2**n):
    a = [0] * (m + 1)
    com = i
    for j in range(n):
        if com >= (2**(n - j - 1)):
            com -= 2**(n - j - 1)
            for k in range(m + 1):
                a[k] += c[j][k]
    price = a[0]
    del a[0]
    if all(a[j] >= x for j in range(m)):
        ans.append(price)
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))
