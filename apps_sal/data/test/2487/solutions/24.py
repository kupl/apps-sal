import numpy as np
N = int(input())
num = 0
for i in range(1, N + 1):
    num += i * (N + 1 - i)
for _ in range(N - 1):
    (u, v) = map(int, input().split())
    (x, y) = (min(u, v), max(u, v))
    num -= (N + 1 - y) * x
print(num)
