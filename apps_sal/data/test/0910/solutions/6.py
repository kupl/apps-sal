import sys

# sys.stdin = open("ivo.in")
n, a, b = list(map(int, sys.stdin.readline().split()))

if n > a * b:
  print(-1)
  return

res = []
for i in range(a):
  res.append([])
  for j in range(b):
    res[i].append(0)
for i in range(n):
  res[i // b][i % b] = i + 1

for j in range(1, a, 2):
  res[j].reverse()

for i in range(a):
  print(" ".join(map(str, res[i])))

