import bisect
from itertools import accumulate
import sys
input = sys.stdin.readline

N, A, R, M = list(map(int, input().split()))
W = sorted(map(int, input().split()))
SUM = list(accumulate(W))
SW = SUM[-1]

indmin = 0
indmax = 1
ANS = 1 << 62


def calc(MINUS, PLUS, A, R, M):

    RET1 = MINUS * A + PLUS * R
    MIN = min(MINUS, PLUS)

    RET2 = MIN * M + (MINUS - MIN) * A + (PLUS - MIN) * R

    return min(RET1, RET2)


while indmin < N:
    while indmax < N and W[indmax] == W[indmin]:
        indmax += 1

    ave = W[indmin]
    MINUS = ave * (indmin + 1) - SUM[indmin]
    PLUS = SW - SUM[indmax - 1] - ave * (N - indmax)

    ANS = min(ANS, calc(MINUS, PLUS, A, R, M))

    indmin = indmax
    indmax += 1

AVE = SW // N

for ave in range(max(W[0], AVE - 10**4), min(AVE + 10**4, W[-1])):
    indmin = bisect.bisect_left(W, ave)
    if W[indmin] == ave:
        continue
    indmin, indmax = indmin - 1, indmin

    MINUS = ave * (indmin + 1) - SUM[indmin]
    PLUS = SW - SUM[indmax - 1] - ave * (N - indmax)

    ANS = min(ANS, calc(MINUS, PLUS, A, R, M))


print(ANS)
