import numpy as np
(a, b) = map(int, input().split())
A = ''.join([str(a)] * b)
B = ''.join([str(b)] * a)
print(min(A, B))
