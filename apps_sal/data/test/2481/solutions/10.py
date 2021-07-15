import heapq
h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]
flag = [[1 for _ in range(10)] for _ in range(10)]
for i in range(10):
    que = [[0, i]]
    while que:
        now = heapq.heappop(que)
        flag[i][now[1]] = 0
        for j in range(10):
            if flag[i][j]:
                heapq.heappush(que, [c[i][now[1]]+ c[now[1]][j], j])
                if c[i][now[1]]+c[now[1]][j] < c[i][j]:
                    c[i][j] = c[i][now[1]]+ c[now[1]][j]

ans = 0      
for i in range(h):
    for j in range(w):
        if a[i][j] != -1:
            ans += c[a[i][j]][1]
print(ans)
