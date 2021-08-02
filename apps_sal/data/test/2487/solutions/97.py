import numpy as np
N = int(input())
num = 0
for i in range(1, N + 1):
    num += i * (N + 1 - i)
for _ in range(N - 1):
    u, v = sorted(map(int, input().split()))
    num -= (N + 1 - v) * u
print(num)
