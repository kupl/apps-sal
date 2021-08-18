
a = []
k = []

n, m = map(int, input().split())
for i in range(n + 1):
    if i < n:
        a.append(input())
    k.append([0 for j in range(m + 1)])

ans = 0

for i in range(n - 1, -1, -1):
    add = 0
    for j in range(m - 1, -1, -1):
        sign = 1
        if a[i][j] == 'B':
            sign = -1
        k[i][j] = add + k[i + 1][j]
        if k[i][j] != sign:
            ans += 1
            add += sign - k[i][j]
            k[i][j] = sign

print(ans)
