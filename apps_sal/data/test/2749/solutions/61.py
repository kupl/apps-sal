import numpy as np

H, W = list(map(int, input().split()))
N = int(input())
A = list(map(int, input().split()))

out = []

for i, a in enumerate(A):
    for j in range(a):
        out.append(i + 1)

# print(out)
out = np.array(out).reshape((H, W))
# print(out, out.shape)

sign = 1
for li in out:
    print((*li[::sign]))
    sign *= -1
