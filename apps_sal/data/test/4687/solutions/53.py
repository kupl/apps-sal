from collections import defaultdict as dd
from itertools import count
(N, K) = map(int, input().split())
Cnt = dd(lambda: 0)
for _ in range(N):
    (a, b) = map(int, input().split())
    Cnt[a] += b
num = 0
for i in count(1, 1):
    num += Cnt[i]
    if num >= K:
        print(i)
        break
