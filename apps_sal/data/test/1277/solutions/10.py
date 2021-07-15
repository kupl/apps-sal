import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, u, v = map(int, input().split())
u -= 1
v -= 1
Tree = [[] for _ in range(N)]

for _ in range(N-1):
  A, B = map(lambda x:int(x)-1, input().split())
  Tree[A].append(B)
  Tree[B].append(A)

#u-v間の単純pathを用意する
path = []
def connected(v, tv, p=-1):
  if v == tv:
    return True
  for w in Tree[v]:
    if w == p:
      continue
    elif connected(w, tv, v):
      path.append(w)
      return True
  return False

connected(v, u)
path.append(v)

#u-v間の点からvとは逆方向にdfs
#u-vの中点から調べれば十分(中点よりvに寄ると、青木君は捕まってしまう)

def dfs(v, p):
  d = -1
  for w in Tree[v]:
    if w == p:
      continue
    else:
      d = max(d, dfs(w, v))
  return d + 1

dist = len(path)
mid = path[dist//2 - 1]
par = path[dist//2]
ans = dfs(mid, par)

print(ans + (dist-1)//2)
