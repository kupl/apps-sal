(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
g = [a[i::m] for i in range(m)]
for i in range(m):
    for j in range(1, len(g[i])):
        g[i][j] += g[i][j - 1]
ans = [0]
for i in range(n):
    ans.append(ans[-1] + g[i % m][i // m])
print(*ans[1:])
