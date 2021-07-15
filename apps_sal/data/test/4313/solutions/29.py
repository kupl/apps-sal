N = int(input())
V = list(map(lambda v: int(v), input().split(" ")))
C = list(map(lambda c: int(c), input().split(" ")))
s = 0
for i in range(N):
  d = V[i] - C[i]
  s += max([d,0])

print(s)
