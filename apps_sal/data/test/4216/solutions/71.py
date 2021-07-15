import math
N = int(input())
lim = math.floor(math.sqrt(N))
f_min = len(str(N))
for i in range(1, lim + 1):
  if N % i == 0:
    B = int(N / i)
    if len(str(B)) < f_min:
      f_min = len(str(B))
print(f_min)

