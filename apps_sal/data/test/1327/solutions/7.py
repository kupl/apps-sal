from itertools import product

N, M = map(int, input().split())
L = [[] for _ in range(N)]

for i in range(N):
  x, y, z = map(int, input().split())
  L[i] += [x, y, z]

ans = 0

for pm in product([-1, 1], repeat=3):
  temp = []
  for l in L:
    temp.append(pm[0]*l[0] + pm[1]*l[1] + pm[2]*l[2])
  temp.sort(reverse = True)
  ans = max(ans, sum(temp[:M]))

print(ans)
