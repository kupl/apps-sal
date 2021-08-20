from collections import defaultdict
from bisect import bisect_left
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
D = defaultdict(int)
for i in A:
    D[i] += 1
for _ in range(M):
    (a, b) = map(int, input().split())
    D[b] += a
D_sorted = sorted(D.items(), key=lambda x: x[0], reverse=True)
ans = 0
count = 0
for (x, c) in D_sorted:
    if count + c < N:
        ans += x * c
        count += c
    else:
        ans += x * (N - count)
        break
print(ans)
