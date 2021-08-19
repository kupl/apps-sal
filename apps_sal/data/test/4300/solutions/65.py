import itertools as it
# 入力
N = int(input())
d = list(map(int, input().split()))

# 2つの組み合わせの全パターンを取得する
k = list(it.combinations(d, 2))
# 組み合わせの掛け算をリストに詰めてsum
n = [a * b for a, b in k]

print(sum(n))
