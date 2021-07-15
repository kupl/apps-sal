N = int(input())
x, y = map(int, input().split())
d = [x - y, x - y, x + y, x + y]
for i in range(1,N):
  x, y = map(int, input().split())
  d[0] = max(d[0], x-y)
  d[1] = min(d[1], x-y)
  d[2] = max(d[2], x+y)
  d[3] = min(d[3], x+y)
print(max(d[0]-d[1], d[2]-d[3]))
