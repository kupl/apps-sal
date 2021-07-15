H,W = list(map(int,input().split()))

S = [input() for i in range(H)]

for i in range(H):
  for j in range(W):
    if S[i][j] != "#":
      continue
    for y,x in ((0,1),(0,-1),(1,0),(-1,0)):
      if 0 <= i + y < H and 0 <= j + x < W:
        if S[i + y][j + x] == "#":
          break
    else:
      print("No")
      return
print("Yes")

