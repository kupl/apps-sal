import sys
sys.setrecursionlimit(10**7)

N = int(input())
links = [[] for _ in range(N)]
result = [0 for _ in range(N)]
memo = [0 for _ in range(N)]
for _ in range(N-1):
  u, v, w = map(int, input().split())
  u -= 1
  v -= 1
  links[u].append([v, w])
  links[v].append([u, w])
def color(u):
  if memo[u]:
    return
  for l in links[u]:
    result[l[0]] = abs(l[1]%2-result[u])
  memo[u] = 1
  for l in links[u]:
    color(l[0])
color(0)
for r in result:
  print(r)
