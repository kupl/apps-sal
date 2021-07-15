from collections import defaultdict
class Graph:
 def __init__(self,v):
  self.adj=defaultdict(list)
  self.V = v
 def findstep(self,s):
  visit = [0]*(self.V)
  dist =[0]*self.V
  q = []
  q.append(0)
  while q:
   t = q.pop(0)
   visit[t] =1
   for i in self.adj[s[t]]:
    if visit[i] == 0 and i != t:
      q.append(i)
      visit[i] = 1
      dist[i] = dist[t] + 1
   self.adj[s[t]] = []
   if t > 0 and visit[t-1] == 0:
    q.append(t-1)
    visit[t-1]= 1
    dist[t-1] = dist[t] + 1
   if t < self.V -1 and visit[t+1] == 0:
    q.append(t+1)
    visit[t+1]= 1
    dist[t+1] = dist[t] + 1
  return dist[-1]
s = list(map(int, input().strip()))
n = len(s)
g = Graph(n)
for i in range(n):
 g.adj[s[i]].append(i)
print(g.findstep(s))



