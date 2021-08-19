from collections import Counter

# 入力 (各文字列をソートしておく)
N = int(input())
S = [''.join(sorted(input())) for _ in range(N)]

# Counter でヒストグラムに
num = Counter(S)

# 各文字列ごとに個数 x を扱う
result = sum(x * (x - 1) // 2 for x in num.values())
print(result)
