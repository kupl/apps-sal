import sys
import math


N, H = [int(x) for x in input().split()]
A = []
B = []
for _ in range(N):
    a, b = [int(x) for x in input().split()]
    A.append(a)
    B.append(b)
B.sort(reverse=True)
max_a = max(A)
cnt = 0
for b in B:
    if b < max_a:
        break
    H -= b
    cnt += 1
    if H <= 0:
        print(cnt)
        return
cnt += int(math.ceil(H / max_a))
print(cnt)
