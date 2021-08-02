import bisect
from itertools import accumulate
N, X = list(map(int, input().split()))
L = list(map(int, input().split()))
Lsum = list(accumulate(L))
ind = bisect.bisect_right(Lsum, X)
print((ind + 1))
