N = int(input())
dic = [0] * N
dist = [[0] * N for i in range(N)]
for i in range(N):
    dic[i] = [int(c) for c in input().split()]
    for j in range(N):
        dist[i][j] = dic[i][j]
    dic[i][i] = float('inf')

ans = 0
for i in range(N):
    for j in range(i):
        d = min(a + b for a, b in zip(dic[i], dic[j]))
        if d < dic[i][j]:
            print(-1)
            return
        elif d > dic[i][j]:
            ans += dic[i][j]
print(ans)
