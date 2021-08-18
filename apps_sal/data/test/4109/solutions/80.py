n, m, x = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]
ans = []
for i in range(2**n):
    a = [0] * m
    price = 0
    for j in range(n):
        if ((i >> j) & 1):
            for k in range(m):
                a[k] += c[j][k + 1]
            price += c[j][0]
    if all(j >= x for j in a):
        ans.append(price)

if len(ans) == 0:
    print("-1")
else:
    print(min(ans))
