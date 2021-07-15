import bisect
from collections import deque
N, K = map(int, input().split())
a = sorted(map(int, input().split()))

# K以上のカードは単体で条件を満たすから考えない
a_k = bisect.bisect_left(a, K, lo=0, hi=N)
A = a[:a_k][::-1]
tmp = 0
N = result = N-(N-a_k)

for n, i in enumerate(A):
    if tmp+i >= K:
        result = N-(n+1)
    else:
        tmp += i

print(result)
