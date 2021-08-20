import bisect
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
mod = 1000000007


def Combi(a, b):
    if b > a:
        return 0
    ANS = 1
    for i in range(min(b, a - b)):
        ANS = ANS * (a - i) * pow(min(b, a - b) - i, mod - 2, mod) % mod
    return ANS % mod


def alltuple(A):
    ANS = []
    MAX = max(A)
    if min(A) != -1:
        return [tuple(A)]
    LEN = len(A)
    for i in range(LEN):
        if A[i] == -1:
            if MAX != -1:
                A[i] = MAX
                ANS += alltuple(A)
            A[i] = MAX + 1
            ANS += alltuple(A)
            A[i] = -1
    return ANS


ALLX = set(alltuple([-1] * N))


def LIS(A):
    LEN = len(A)
    DP = [float('inf')] * LEN
    for a in A:
        pos = bisect.bisect_left(DP, a)
        DP[pos] = a
    ANS = 0
    for i in range(LEN):
        if DP[i] != float('inf'):
            ANS = i
    return ANS + 1


ANS = 0
KOSUU = 0
for tu in ALLX:
    LIS_tu = LIS(tu)
    B = []
    for i in range(max(tu) + 1):
        MIN = 1 << 30
        for j in range(N):
            if tu[j] == i:
                MIN = min(MIN, A[j])
        B.append(MIN)
    for i in range(len(B) - 2, -1, -1):
        B[i] = min(B[i], B[i + 1])
    SB = [0] + sorted(set(B))
    compression_dict = {a: ind for (ind, a) in enumerate(SB)}
    BC = [compression_dict[m] for m in B]
    LEN = len(B)
    DPLEN = len(SB)
    DP = [[0] * DPLEN for i in range(LEN + 1)]
    DP[0][0] = 1
    for i in range(LEN):
        for j in range(DPLEN):
            if DP[i][j] == 0:
                continue
            for k in range(j + 1, DPLEN):
                if k > BC[i]:
                    break
                for l in range(i + 1, LEN + 1):
                    DP[l][k] += DP[i][j] * Combi(SB[k] - SB[k - 1], l - i)
                    DP[l][k] %= mod
    KOSUU += sum(DP[-1])
    ANS += sum(DP[-1]) * LIS_tu
print(ANS * pow(KOSUU, mod - 2, mod) % mod)
