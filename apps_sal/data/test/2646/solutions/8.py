from collections import deque
N, M = map(int, input().strip().split())
l = []
dp = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().strip().split())
    l.append((a, b))
    dp[a - 1].append(b)
    dp[b - 1].append(a)

d = deque([1])
visited = [0 for _ in range(N)]
visited[0] = 1
cnt = 1
while d:
    tmp = d.popleft()
    for e in dp[tmp - 1]:
        if visited[e - 1] == 0:
            visited[e - 1] = tmp
            cnt += 1
            d.append(e)

if cnt != len(visited):
    print("No")
else:
    print("Yes")
    for n in range(1, N):
        print(visited[n])
