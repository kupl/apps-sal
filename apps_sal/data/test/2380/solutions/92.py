import copy
from collections import Counter
N, M = map(int, input().split())
A = list(map(int, input().split()))
counter = Counter(A)
for _ in range(M):
    B, C = map(int, input().split())
    counter[C] = counter.get(C, 0) + B

ans = 0
for x in sorted(counter, reverse=True):
    if counter[x] >= N:
        ans += x * N
        break
    else:
        ans += x * counter[x]
        N -= counter[x]
print(ans)
