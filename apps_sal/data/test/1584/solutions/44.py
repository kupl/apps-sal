import bisect
from copy import deepcopy
N = int(input())
L = sorted(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i + 1, N - 1):
        b = L[j] + L[i]
        x = bisect.bisect_left(L, b) - j - 1
        if x > 0:
            ans += x

print(ans)
