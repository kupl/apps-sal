from math import log2

N = int(input())

m = 0
a = 0

for i in range(1, N + 1):
  l = log2(i)
  if l % 1 == 0:
    m = i


print(m)

