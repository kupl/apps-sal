import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
A = list(map(int, input().split()))

A = [a - 1 for a in A]

MININDLIST = [[i] * m for i in range(m)]

for i in range(m):
    MIN = A[i]
    MININDNOW = i
    for j in range(i, m):
        if A[j] < MIN:
            MIN = A[j]
            MININDNOW = j

        MININDLIST[i][j] = MININDNOW

mod = 998244353

SCORE = [0] * ((m + 1)**2)


def calc(i, j, m):
    if SCORE[i * (m + 1) + j] != 0:
        return SCORE[i * (m + 1) + j]

    # print(i,j)
    if j == i + 1 or i == j:
        return 1

    MININD = MININDLIST[i][j - 1]

    # print(MININD)

    ANS1 = ANS2 = 0

    for mi in range(i, MININD + 1):
        ANS1 = (ANS1 + calc(i, mi, m) * calc(mi, MININD, m)) % mod

    for Mi in range(MININD + 1, j + 1):
        ANS2 = (ANS2 + calc(MININD + 1, Mi, m) * calc(Mi, j, m)) % mod

    SCORE[i * (m + 1) + j] = ANS1 * ANS2 % mod

    return SCORE[i * (m + 1) + j]


print(calc(0, m, m))
