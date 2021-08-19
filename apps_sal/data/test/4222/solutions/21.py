import itertools

N, K = map(int, input().split())
# 2次元配列
d = []
A = []
for i in range(K):
    d.append(int(input()))
    array = list(map(int, input().strip().split()))
    A.append(array)

# A[][]からの要素を取り出して重複しないリストXを作りたい
X = list(itertools.chain.from_iterable(A))
X = list(set(X))

# Xはお菓子をもらった人のリスト
print(N - len(X))
