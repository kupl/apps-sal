import heapq
INF = 10**10
n = int(input())
a = [[int(item) for item in input().split()] for _ in range(n)]
b = [[INF for _ in range(n)] for _ in range(n)]

ans = 0
for i in range(n):
    ans += sum(a[i])
    a[i][i] = INF
ans //= 2

for i in range(n):
    for j in range(i):
        bipas = min(map(sum, zip(a[i], a[j])))
        if a[i][j] > bipas:
            print(-1)
            return
        if a[i][j] == bipas:
            ans -= a[i][j]
print(ans)
