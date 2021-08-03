from collections import Counter
import bisect
N = int(input())
A = list(map(int, input().split()))
C = list(Counter(A).values())
C.sort()
L = len(C)

# Cのうちx以上のものの個数D[x]を計算(x=0,...,N)
D = [L - bisect.bisect_left(C, x) for x in range(N + 1)]
S = [0]
for n in range(1, N + 1):
    S.append(S[-1] + D[n])

# T[x]=S[x]/x(x=1,...,N)としてKをbisect_rightで挿入した時のindexが答え
T = [x / S[x] for x in range(1, N + 1)]
for K in range(1, N + 1):
    print(bisect.bisect_right(T, 1 / K))
