from collections import deque

X,Y,A,B,C = map(int, input().split())
A=[int(a) for a in input().split()]
B=[int(b) for b in input().split()]
C=[int(c) for c in input().split()]

A=sorted(A, reverse=True)[:X]
B=sorted(B, reverse=True)[:Y]
AB=deque(sorted(A+B))

for c in sorted(C, reverse=True):
  if c >= AB[0]:
    AB.popleft()
    AB.append(c)
  else:
    break

print(sum(AB))
