from bisect import bisect_left
from numpy import cumsum

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
B_ = [0] * N
ans = 0
start = 0
for i, b in enumerate(B):
    j = bisect_left(A, b, start)
    B_[i] = j
    start = j
B_ = cumsum(B_)
start = 0
for c in C:
    i = bisect_left(B, c, start)
    start = i
    if i != 0:
        ans += B_[i - 1]
print(ans)
