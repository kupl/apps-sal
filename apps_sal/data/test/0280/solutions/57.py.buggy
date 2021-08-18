from itertools import permutations
import bisect
from operator import itemgetter
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
W = list(map(int, input().split()))
B = [tuple(map(int, input().split())) for i in range(M)]

MIN = 1 << 60
for l, v in B:
    MIN = min(MIN, v)

if MIN < max(W):
    print((-1))
    return

B2 = []
for x, y in B:
    B2.append([y, x])
B2.sort(key=itemgetter(0))

B3 = [B2[0]]
for x, y in B2[1:]:
    if y <= B3[-1][1]:
        continue
    else:
        B3.append([x, y])

B3 = [[0, 0]] + B3
B3.append([1 << 60, B3[-1][1]])


L = list(permutations(list(range(N))))
ANS = 1 << 60

for l in L:
    W2 = [W[l[i]] for i in range(N)]
    DP = [0] * (N + 1)

    # if W2!=[857,849,806,57,608,244,349,513]:
    #    continue

    for i in range(N):
        for j in range(i + 1, N):
            S = sum(W2[i:j + 1])
            x = bisect.bisect(B3, [S, 0])

            DP[j] = max(DP[j], DP[i] + B3[x - 1][1])

        # print(W2,S,x,DP)

    # if W2==[857,849,806,57,608,244,349,513]:
    #    print(W2,DP)

    ANS = min(ANS, DP[N - 1])
print(ANS)
