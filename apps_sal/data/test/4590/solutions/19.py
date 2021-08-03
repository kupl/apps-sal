from itertools import accumulate
from bisect import bisect_right
N, M, K = map(int, input().split())
A = [0] + list(accumulate(map(int, input().split()), lambda x, y: x + y))
B = [0] + list(accumulate(map(int, input().split()), lambda x, y: x + y))
ans = 0
for i in range(N + 1):
    left = K - A[i]
    if left < 0:
        break
    j = bisect_right(B, left)
    ans = max(ans, i + j - 1)
print(ans)
