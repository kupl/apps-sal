import numpy as np
 
N = int(input())
F = np.array([list(map(int, input().split(' '))) for _ in range(N)])
P = np.array([list(map(int, input().split(' '))) for _ in range(N)])
 
ans = - (10 ** 11)
 
for n in range(1, 1024):
    bits = np.array(list(map(int, list('{:010b}'.format(n)))))
    dup = np.sum(F * bits, axis=1)
    ans = max(ans, np.sum(P[range(N), dup]))

print(ans)
