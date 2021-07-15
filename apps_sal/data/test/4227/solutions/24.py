N,M=map(int, input().split())

checked = [0] * 8
path = [[] for _ in range(8)]

for i in range(M):
  a,b=map(int, input().split())
  path[a-1].append(b-1)
  path[b-1].append(a-1)

ans = 0

def dfs(place):
  checked[place] = 1
  if sum(checked) == N:
    return 1
  ret = 0
  for i in path[place]:
    if checked[i] == 1:
      continue
    ret += dfs(i)
    checked[i] = 0
  return ret

print(dfs(0))
