import sys
from sys import stdin
input = stdin.readline
sys.setrecursionlimit(20000000)
 
 
def main():
  N = int(input())
  G = [[] for _ in range(N+1)]
  for i in range(N-1):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))
 
  color = [-1]*(N+1)
  color[1] = 0
  # S = [1]
  # while len(S):
  #   now = S[-1]
  #   for next_, w in G[now]:
  #     if color[next_] != -1:
  #       continue
  #     S.append(next_)
  #     color[next_] = (w % 2) ^ color[now]
  #     break
  #   else:
  #     S.pop()
 
  def dfs(now):
    for next_, w in G[now]:
      if color[next_] == -1:
        color[next_] = (w % 2) ^ color[now]
        dfs(next_)
  dfs(1)
 
  for i in range(1, N+1):
    print(color[i])
 
 
if(__name__ == '__main__'):
  main()
