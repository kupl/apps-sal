import itertools
import bisect
(n, x) = map(int, input().split())
ll = list(map(int, input().split()))
dl = [0] + list(itertools.accumulate(ll))
print(bisect.bisect_right(dl, x))
