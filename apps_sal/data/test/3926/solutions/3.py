from collections import deque
n, m = list(map(int, input().split()))
sx, sy = list(map(int, input().split()))
x, y = list(map(int, input().split()))
smap = [input() for i in range(n)]


mp = [[-1] * m for i in range(n)]


sx, sy = sx - 1, sy - 1
mp[sx][sy] = 0
ans = 0

q = deque()

q.append((sx, sy))


def move(px, py, s, left):
  if (px >= 0 and px < n and py >= 0 and py < m):
    if (smap[px][py] == '.' and mp[px][py] == -1):
      mp[px][py] = s
      if left:
        q.appendleft((px, py))
      else:
        q.append((px, py))



while q:
  px, py = q.popleft()
  s = mp[px][py]
  #print(s)
  #print(s + py - r)
  #print(s - py + r)
  #print(s + py - r <= y * 2)
  #print(s - py + r <= x * 2)
  #print(x, y)
  #return
  ans += s + py - sy <= y * 2 and s - py + sy <= x * 2
  
  move(px + 1, py, s, left=True)
  move(px - 1, py, s, left=True)
  move(px, py + 1, s + 1, left=False)
  move(px, py - 1, s + 1, left=False)
  
print(ans)

