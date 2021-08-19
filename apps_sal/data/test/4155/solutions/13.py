import numpy as np
N = int(input())
h = list(map(int, input().split()))
s = h[0]
for i in range(N - 1):
    if h[i] <= h[i + 1]:
        s = s + h[i + 1] - h[i]
print(s)
