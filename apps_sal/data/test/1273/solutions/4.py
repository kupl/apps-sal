from collections import deque

def main():
  n = int(input())
  graph=[[] for _ in range(n+1)]
  for i in range(1,n):
    a,b = map(int, input().split())
    d1 = {"id":i,"to":b}
    d2 = {"id":i,"to":a}
    graph[a].append(d1)
    graph[b].append(d2)
  
  k = 0
  root = 1
  for i in range(1, n+1):
    if k < len(graph[i]):
      root = i
      k = max(k, len(graph[i]))
  print(k)
  q=deque([root])
  color=[[] for _ in range(n+1)]
  reached=[False]*(n+1)
  ans=[0]*(n)
  while q:
    current = q.popleft()
    reached[current] = True
    temp = 1
    for dic in graph[current]:
      id = dic["id"]
      next = dic["to"]
      if reached[next]:
        continue
      while temp in color[current]:
        temp += 1
      color[next].append(temp)
      ans[id] = temp
      temp += 1
      q.append(next)
  for i in ans[1:]:
    print(i)
      
def __starting_point():
  main()
__starting_point()
