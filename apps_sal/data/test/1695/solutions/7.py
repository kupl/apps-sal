n, m = list(map(int, input().split()))
u = []
for i in range(n):
    u.append(list(input()))
a = list(map(int, input().split()))
ans = 0
for j in range(m):
    d = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    for i in range(n):
        d[u[i][j]] += 1
    ans += a[j] * max(d['A'], d['B'], d['C'], d['D'], d['E'])
print(ans)
