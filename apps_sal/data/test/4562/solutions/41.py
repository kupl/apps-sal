import math
N = int(input())
for i in range(N):
  x = N - i
  if int(math.sqrt(x)) == math.sqrt(x):
    print(x)
    break

