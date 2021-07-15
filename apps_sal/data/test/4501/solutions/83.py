from collections import defaultdict

N, A = map(int, input().split())
X = list(map(int, input().split()))
X =[x - A for x in X]

d = defaultdict(int)
d[0] = 1

for x in X:
  for k, v in list(d.items()):
    d[k+x] += v

print(d[0]-1)
