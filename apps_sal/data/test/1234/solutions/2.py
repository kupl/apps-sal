n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append((a[i], i + 1))
b.sort(reverse=True)
c = b[: m * k]
c.sort(key=lambda x: x[1])

ans = 0
for i in c:
    ans += i[0]

print(ans)
for i in range(len(c) - 1):
    if (i + 1) % m == 0:
        print(c[i][1], end=' ')
