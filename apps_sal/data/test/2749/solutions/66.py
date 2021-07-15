import numpy as np
H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

B = []
for i, a in enumerate(A, start=1):
    for _ in range(a):
        B.append(i)

B = np.array(B)
B = B.reshape(H, W)

for h in range(H):
    if h % 2 == 1:
        B[h] = B[h, ::-1]

for b in B:
    print(*b)
