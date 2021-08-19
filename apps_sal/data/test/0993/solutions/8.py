import itertools
import collections
(N, M) = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
cum = [0] + [c % M for c in itertools.accumulate(A)]
cnt = collections.Counter(cum)
ans = sum((v * (v - 1) // 2 for v in list(cnt.values())))
print(ans)
