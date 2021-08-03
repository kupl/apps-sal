a = []
k = []

n, m = map(int, input().split())
for i in range(n + 1):
    if i < n:
        a.append([-1 if c == 'B' else 1 for c in input()])
    k.append([0 for j in range(m)])

ans = 0

for i in reversed(range(n)):
    add = 0
    for j in reversed(range(m)):
        k[i][j] = add + k[i + 1][j]
        if k[i][j] != a[i][j]:
            ans += 1
            add += a[i][j] - k[i][j]
            k[i][j] = a[i][j]

print(ans)
