import numpy as np
N = int(input())
num = N * (N+1) * (N+2) // 6
for _ in range(N-1):
  u, v = sorted(map(int, input().split()))
  num -= (N+1-v) * u
print(num)
