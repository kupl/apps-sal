from queue import deque

H, W = map(int,input().split())
S = list(list(input()) for _ in range(H))
ans = 0

for h in range(H):
  for w in range(W):
    if S[h][w] == ".":
      D = [[-1] * W for _ in range(H)]
      D[h][w] = 0
      Q = deque()
      Q.append((h, w))
      
      while Q:
        y, x = Q.popleft()

        for i, j in (1, 0), (-1, 0), (0, 1), (0, -1):
          y2, x2 = y + i, x + j

          if 0 <= y2 < H and 0 <= x2 < W and S[y2][x2] == "." and D[y2][x2] == -1:
            Q.append((y2, x2))
            D[y2][x2] = D[y][x] + 1

      for i in range(H): ans = max(ans, max(D[i]))

print(ans)
