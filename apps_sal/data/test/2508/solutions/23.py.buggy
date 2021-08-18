#import heapq
from collections import deque
h, w, k = list(map(int, input().split()))
x1, y1, x2, y2 = list(map(int, input().split()))
x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
dp = [[-1] * w for _ in range(h)]
#que = []
que = deque()
c = [input() for _ in range(h)]

dp[x1][y1] = 0
#heapq.heappush(que, (dp[x1][y1], [x1,y1]))
que.append((x1, y1))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while que:
    x, y = que.popleft()
    if x == x2 and y == y2:
        print(dp[x][y])
        return
    for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        for i in range(1, k + 1):
            xx = x + dx * i
            yy = y + dy * i
            if not(0 <= xx < h and 0 <= yy < w) or c[xx][yy] == "@":
                break
            if 0 <= dp[xx][yy] <= dp[x][y]:
                break
            if dp[xx][yy] == -1:
                que.append((xx, yy))
            dp[xx][yy] = dp[x][y] + 1
print(-1)
