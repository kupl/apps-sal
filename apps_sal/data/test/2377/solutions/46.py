import math
N, H = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())
aa = sorted(A, key=lambda x: -x)
bb = sorted(B, key=lambda x: -x)
ans = 0
I = H
mh = max(aa)
for x in bb:
    if (x < mh):
        break
    I = I - x
    ans += 1
    if (I <= 0):
        break
if (I > 0):
    ans += math.ceil(I / max(aa))
print(ans)
