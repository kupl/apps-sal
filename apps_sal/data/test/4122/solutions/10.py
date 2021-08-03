from itertools import accumulate
import sys
input = sys.stdin.readline

H, n = list(map(int, input().split()))
D = list(map(int, input().split()))

ONETURN = list(accumulate(D))

MIN = min(ONETURN)
ONE = ONETURN[-1]

if ONE >= 0:
    if H + MIN > 0:
        print(-1)
        return

    DAMAGED = [H + o for o in ONETURN]
    for i in range(n):
        if DAMAGED[i] <= 0:
            print(i + 1)
            return

ANS = 0

R = max(0, (H + MIN) // (-ONE))
ANS += R * n
H += R * ONE

while H + MIN > 0:
    H += ONE
    ANS += n

DAMAGED = [H + o for o in ONETURN]
for i in range(n):
    if DAMAGED[i] <= 0:
        print(ANS + i + 1)
        break
