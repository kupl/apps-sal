import numpy as np
n,k,q = map(int, input().split())
p = np.full(n, k, dtype=np.int)
first = 0
for i in range(q):
    a = int(input())
    p -= 1
    p[a-1] += 1
for i in p:
    if i <= 0:
        print("No")
    else:
        print("Yes")
