H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())

Ch += 1
Cw += 1
Dh += 1
Dw += 1


S = ['#'*(W+4)]
S.append('#'*(W+4))
for k in range(H):
  S.append('##' + input() + '##')
S.append('#'*(W+4))
S.append('#'*(W+4))

foo = [[-1 for _ in range(W+4)] for _ in range(H+4)]
for k in range(2, H+2):
  for j in range(2, W+2):
    if S[k][j] == '.':
      foo[k][j] = 10**6

foo[Ch][Cw] = 0

now = []
new = [(Ch, Cw)]
while len(new) > 0:
  item = new.pop()
  now.append(item)
  x = item[0]
  y = item[1]
  if foo[x+1][y] == 10**6:
    foo[x+1][y] = 0
    new.append((x+1, y))
  if foo[x][y+1] == 10**6:
    foo[x][y+1] = 0
    new.append((x, y+1))
  if foo[x-1][y] == 10**6:
    foo[x-1][y] = 0
    new.append((x-1, y))
  if foo[x][y-1] == 10**6:
    foo[x][y-1] = 0
    new.append((x, y-1))


ans = 0
while foo[Dh][Dw] == 10**6:
  if len(now) == 0:
    print(-1)
    return 
  ans += 1
  while len(now) > 0:
    item = now.pop()
    x = item[0]
    y = item[1]
    if foo[x+2][y+2] > ans:
      foo[x+2][y+2] = ans
      new.append((x+2, y+2))
    if foo[x+2][y+1] > ans:
      foo[x+2][y+1] = ans
      new.append((x+2, y+1))
    if foo[x+2][y] > ans:
      foo[x+2][y] = ans
      new.append((x+2, y))
    if foo[x+2][y-1] > ans:
      foo[x+2][y-1] = ans
      new.append((x+2, y-1))
    if foo[x+2][y-2] > ans:
      foo[x+2][y-2] = ans
      new.append((x+2, y-2))
    if foo[x+1][y+2] > ans:
      foo[x+1][y+2] = ans
      new.append((x+1, y+2))
    if foo[x+1][y-2] > ans:
      foo[x+1][y-2] = ans
      new.append((x+1, y-2))
    if foo[x][y+2] > ans:
      foo[x][y+2] = ans
      new.append((x, y+2))
    if foo[x][y-2] > ans:
      foo[x][y-2] = ans
      new.append((x, y-2))
    if foo[x-2][y+2] > ans:
      foo[x-2][y+2] = ans
      new.append((x-2, y+2))
    if foo[x-2][y+1] > ans:
      foo[x-2][y+1] = ans
      new.append((x-2, y+1))
    if foo[x-2][y] > ans:
      foo[x-2][y] = ans
      new.append((x-2, y))
    if foo[x-2][y-1] > ans:
      foo[x-2][y-1] = ans
      new.append((x-2, y-1))
    if foo[x-2][y-2] > ans:
      foo[x-2][y-2] = ans
      new.append((x-2, y-2))
    if foo[x-1][y+2] > ans:
      foo[x-1][y+2] = ans
      new.append((x-1, y+2))
    if foo[x-1][y-2] > ans:
      foo[x-1][y-2] = ans
      new.append((x-1, y-2))
    if foo[x-1][y-1] > ans:
      foo[x-1][y-1] = ans
      new.append((x-1, y-1))
    if foo[x-1][y+1] > ans:
      foo[x-1][y+1] = ans
      new.append((x-1, y+1))
    if foo[x+1][y+1] > ans:
      foo[x+1][y+1] = ans
      new.append((x+1, y+1))
    if foo[x+1][y-1] > ans:
      foo[x+1][y-1] = ans
      new.append((x+1, y-1))
      
  while len(new) > 0:
    item = new.pop()
    now.append(item)
    x = item[0]
    y = item[1]
    if foo[x+1][y] == 10**6:
      foo[x+1][y] = 0
      new.append((x+1, y))
    if foo[x][y+1] == 10**6:
      foo[x][y+1] = 0
      new.append((x, y+1))
    if foo[x-1][y] == 10**6:
      foo[x-1][y] = 0
      new.append((x-1, y))
    if foo[x][y-1] == 10**6:
      foo[x][y-1] = 0
      new.append((x, y-1))
print(ans)
