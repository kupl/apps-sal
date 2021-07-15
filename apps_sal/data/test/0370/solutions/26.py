K = int(input())
X, Y = list(map(int,input().split()))

if K%2 == 0 and (X+Y)%2:
    print((-1))
    return

def next(x,y):
    if x < 0:
        dx, dy = next(-x, y)
        return -dx, dy
    if y < 0:
        dx, dy = next(x, -y)
        return dx, -dy
    if x < y:
        dx, dy = next(y, x)
        return dy, dx
    if x + y == K:
        return x, y
    if x + y <= K * 2 and (x + y) % 2 == 0:
        return (x + y)//2, (x + y)//2 - K
    return K, 0

x, y = 0,0
ans = list()
while x != X or y != Y:
    dx, dy = next(X - x, Y - y)
    x += dx; y += dy
    ans.append((x, y))

print((len(ans)))
for x, y in ans:
  print((x, y))

