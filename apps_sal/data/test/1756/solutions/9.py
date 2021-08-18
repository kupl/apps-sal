import bisect
from itertools import accumulate
import sys
input = sys.stdin.readline

n, x = list(map(int, input().split()))
D = list(map(int, input().split()))

D2 = [x * (x + 1) // 2 for x in D]


S = [0] + list(accumulate(D + D))
S2 = [0] + list(accumulate(D2 + D2))

ANS = 0


for i in range(2 * n + 1):
    if S[i] - x < 0:
        continue
    y = bisect.bisect_left(S, S[i] - x)

    score = S2[i] - S2[y]
    rest = x - (S[i] - S[y])

    MAX = D[(y - 1) % n]

    score += (MAX + (MAX - rest + 1)) * rest // 2

    ANS = max(ANS, score)

print(ANS)
