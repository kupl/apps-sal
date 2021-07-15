from queue import Queue
import sys
#sys.stdin = open('input.txt')

n, m, k = [int(x) for x in input().split(' ')]

if k&1:
  print('IMPOSSIBLE')
  return

s = [None]*n
for i in range(n):
  s[i] = [None]*m
  t = input()
  for j in range(m):
    s[i][j] = t[j]
    if t[j] == 'X': x, y = j, i

def bfs(x, y):
  res = [[10000000]*m for i in range(n)]
  if s[y][x] == '*': return res
  q = Queue()
  q.put((x, y))
  step = 0

  def add(x, y):
    if res[y][x] != 10000000 or s[y][x] == '*' or step >= res[y][x]: return
    q.put((x, y))
    res[y][x] = step+1

  res[y][x] = step

  while not q.empty():
    x, y = q.get()
    step = res[y][x]
    #print('-')
    if y < n-1: add(x, y+1) #D
    if x > 0: add(x-1, y)   #L
    if x < m-1: add(x+1, y) #R
    if y > 0: add(x, y-1)   #U
  return res

res = bfs(x, y)


path = []
add = lambda s: path.append(s)
for i in range(k):
  step = k-i
  #print(step, (y, x), k-i)
  if y < n-1 and res[y+1][x] <= step: #D
    add('D')
    y = y+1
  elif x > 0 and res[y][x-1] <= step: #L
    add('L')
    x = x-1
  elif x < m-1 and res[y][x+1] <= step: #R
    add('R')
    x = x+1
  elif y > 0 and res[y-1][x] <= step: #U
    add('U')
    y = y-1
  else:
    print('IMPOSSIBLE')
    return

print(str.join('', path))

