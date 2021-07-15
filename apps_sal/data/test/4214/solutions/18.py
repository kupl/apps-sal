import math
import itertools

N = int(input())
arr = []
for _ in range(N):
  x,y = map(int,input().split())
  arr.append((x,y))

p = list(itertools.permutations(arr))

d = 0.0
for pair in p:
  for a, b in zip(pair[0:],pair[1:]):
    d += math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

print(d/len(p))  
