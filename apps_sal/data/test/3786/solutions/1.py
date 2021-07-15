import sys, math

#f = open('input/input_2', 'r')
f = sys.stdin

N = int(f.readline())
pl = list(map(int, f.readline().split()))

e = [[] for _ in range(N+1)]
lv = [0] * (N+1)
for i, p in enumerate(pl):
  e[p].append(i+2)

c = [0] * (N+1)

for i in range(1, N+1):
  c[lv[i]] = 1 - c[lv[i]]
  for j in e[i]:
    lv[j] = lv[i]+1

print(sum(c))

