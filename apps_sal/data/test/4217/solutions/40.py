# ABC118
# B Foods Loved by Everyone 答え見た
# N人、M種類
# iの人はAikだけ好き
# M種類の中にN人全員が好きなものがあるかチェック
# N人分のAikリストを積集合する
import collections
import itertools
N, M = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
for x in A:  # A[0]=kは余計なので削除
    n = x.pop(0)
A = list(itertools.chain.from_iterable(A))
C = collections.Counter(A)
ct = 0
for i in range(1, M + 1):
    if C[i] == N:
        ct += 1
print(ct)
