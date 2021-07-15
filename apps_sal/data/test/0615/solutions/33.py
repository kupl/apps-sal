from itertools import accumulate
from bisect import bisect_left

N = int(input())
A = [int(s) for s in input().split()]
S = [0] + list(accumulate(A))


def score(i, j, k):
    mx = max(S[i], S[j] - S[i], S[k] - S[j], S[N] - S[k])
    mn = min(S[i], S[j] - S[i], S[k] - S[j], S[N] - S[k])
    return mx - mn


ans = float("inf")
i = 1
k = 3
for j in range(2, N - 1):
    while i < j - 1 and abs(S[j] - 2 * S[i]) > abs(S[j] - 2 * S[i+1]):
        i += 1
    while k <= j or k < N - 1 and abs(S[N] - 2 * S[k] + S[j]) > abs(S[N] - 2 * S[k+1] + S[j]):
        k += 1
    mx = max(S[i], S[j] - S[i], S[k] - S[j], S[N] - S[k])
    mn = min(S[i], S[j] - S[i], S[k] - S[j], S[N] - S[k])
    ans = min(ans, mx - mn)
print(ans)

