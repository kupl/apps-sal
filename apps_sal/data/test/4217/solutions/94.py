
# ABC118
# B Foods Loved by Everyone
# N人、M種類
# iの人はAikだけ好き
# M種類の中にN人全員が好きなものがあるかチェック
# N人分のAikリストを積集合する
N, M = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
for x in A:  # A[0]=kは余計なので削除
    n = x.pop(0)
I = set(A[0])  # interesection使うためA[0]をset()
for i in range(1, N):
    # set(a).interesection(b)でaとbの積集合
    I = I.intersection(A[i])  # Iを積集合の結果として、残りのA[i]と比較
print((len(I)))  # 何種類？なのでlen()
