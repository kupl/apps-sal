from itertools import accumulate
from bisect import bisect_left
N, K = map(int, input().split())
A = list(map(int, input().split()))
acc = [0] + list(accumulate(A, lambda x, y: x + y))
ans = 0
for i in range(N + 1):
    j = bisect_left(acc, K + acc[i], lo=i)
    ans += N + 1 - j
print(ans)
