h,w = map(int,input().split())
F = [list(input()) for _ in range(h)]

for i in range(h):
  for j in range(w):
    cnt = 0
    if F[i][j] == '#':
      if 0 <= (i-1) < h: 
        if F[i-1][j] == '#': cnt += 1
      if 0 <= (i+1) < h: 
        if F[i+1][j] == '#': cnt += 1
      if 0 <= (j-1) < w:
        if F[i][j-1] == '#': cnt += 1
      if 0 <= (j+1) < w:
        if F[i][j+1] == '#': cnt += 1
      if cnt == 0:
        print('No')
        return
print('Yes')
