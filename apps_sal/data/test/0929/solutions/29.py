H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
N = 0
A = []
for h in range(H):
  if h % 2 == 0:
    for w in range(W):
      if grid[h][w] % 2:
        if w != W-1:
          grid[h][w] -= 1
          grid[h][w+1] += 1
          A.append([h+1, w+1, h+1, w+2])
          N += 1
        else:
          if h == H-1:
            continue
          grid[h][w] -= 1
          grid[h+1][w] += 1
          A.append([h+1, w+1, h+2, w+1])
          N += 1
          
  else:
    for w in range(W-1, -1, -1):
      if grid[h][w] % 2:
        if w != 0:
          grid[h][w] -= 1
          grid[h][w-1] += 1
          A.append([h+1, w+1, h+1, w])
          N += 1
        else:
          if h == H-1:
            continue
          grid[h][w] -= 1
          grid[h+1][w] += 1
          A.append([h+1, w+1, h+2, w+1])
          N += 1
print(N)
for a in A:
  print(" ".join(map(str, a)))
