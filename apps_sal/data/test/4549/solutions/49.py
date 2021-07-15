H,W = list(map(int,input().split()))

S = ["." * (W + 2)] * (H + 2)

for i in range(H):
  S[i + 1] = "." + input() + "."

for i in range(1, H + 1):
  for j in range(1, W + 1):
    if S[i][j] == "#":
      for x,y in ((0,1),(0,-1),(1,0),(-1,0)):
        if S[i + x][j + y] == "#":
          break
      else:
        print("No")
        return
print("Yes")

