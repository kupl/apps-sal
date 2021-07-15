from collections import defaultdict,deque
import sys
finput=lambda: sys.stdin.readline().strip()

def main():
  n=int(finput())
  edges=[tuple(map(int,finput().split())) for _ in range(n-1)]
  q,k=list(map(int,finput().split()))
  xy=[tuple(map(int,finput().split())) for _ in range(q)]
  ed=defaultdict(deque)
  wt=defaultdict(int)
  for e in edges:
    ed[e[0]].append(e[1])
    ed[e[1]].append(e[0])
    wt[(e[0],e[1])]=e[2]
    wt[(e[1],e[0])]=e[2]
  stack=deque([k])
  cv=stack[0]
  dist=defaultdict(int)
  while stack:
    while ed[cv]:
      if cv!=k:
        if ed[cv][-1]==stack[-1]:
          ed[cv].pop()
          if not ed[cv]:
            break
      stack.append(cv)
      cv=ed[cv].pop()
      dist[cv]=dist[stack[-1]]+wt[(stack[-1],cv)]
    cv=stack.pop()
  for que in xy:
    print((dist[que[0]]+dist[que[1]]))

def __starting_point():
    main()

__starting_point()
