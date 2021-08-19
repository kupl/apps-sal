import numpy as np
(n, k, q) = list(map(int, input().split()))
p = [0] * (n + 1)
for _ in range(q):
    p[int(input())] += 1
for i in range(1, n + 1):
    print('Yes' if k - (q - p[i]) > 0 else 'No')
