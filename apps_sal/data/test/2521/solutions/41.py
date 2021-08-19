from copy import deepcopy
import heapq as hq
with open(0) as f:
    N, *a = map(int, f.read().split())
F = [x for x in a[:N]]  # Fの要素は加えるか取り除くかの2択
C = [x for x in a[N:2 * N]]
B = [-x for x in a[2 * N:]]  # Bの要素は引くか取り除くかの二択
# ヒープにして常に最小値を追跡
hq.heapify(F)
hq.heapify(B)

# Cを二分し、前半はFと、後半はBとで演算を行う
#演算方法(c in C)
# 前半：cがF[0]より大きければF[0]を取り除くN個の一つとし、cをスコアに加える
# 後半：-cがB[0]より大きければB[0]を取り除くN個の一つとし、cをスコアから引く
# どちらも場合も条件を満たさない場合はそのｃを取り除くN個の一つとする
# 計算量：O(N*N*logN)
# 途中計算をメモして計算量軽減
memoF = [0] * (N + 1)  # C[:i]を前半としたときのFとの演算結果の要素和
memoF[0] = sum(F)
memoB = [0] * (N + 1)  # C[i:]を後半としたときのBとの演算結果の要素和
memoB[N] = sum(B)
for i in range(N):
    if C[i] > F[0]:
        memoF[i + 1] = memoF[i] + C[i] - hq.heapreplace(F, C[i])
    else:
        memoF[i + 1] = memoF[i]

    if -C[N - 1 - i] > B[0]:
        memoB[N - 1 - i] = memoB[N - i] - C[N - 1 - i] - hq.heapreplace(B, -C[N - 1 - i])
    else:
        memoB[N - 1 - i] = memoB[N - i]

Scores = [memoF[i] + memoB[i] for i in range(N + 1)]
ans = max(Scores)
print(ans)
