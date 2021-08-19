import numpy as np
N = int(input())
A = list(map(int, input().split()))
a = np.array(A)
b = a - np.arange(1, N + 1)
c = np.median(b)
d = abs(b - c).sum()
print(int(d))
