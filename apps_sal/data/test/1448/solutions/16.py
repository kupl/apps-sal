def F(px, py, ax, ay, bx, by):
  return (bx-ax)*(py-ay)-(by-ay)*(px-ax)


n, d = list(map(int, input().split()))
m = int(input())
for i in range(m):
  x, y = list(map(int, input().split()))
  if F(x, y, d, 0, n, n - d) >= 0 and F(x, y, n, n - d, n - d, n) >= 0 and F(x, y, n - d, n, 0, d) >= 0 and F(x, y, 0, d, d, 0) >= 0:
    print('YES')
  else:
    print('NO')

#(bx-ax)*(py-ay)-(by-ay)*(px-ax)

