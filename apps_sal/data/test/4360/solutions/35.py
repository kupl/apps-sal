import numpy as np

# N, Aを取得
N = int(input())
A = np.array(list(map(int, input().split())))

# 各Aの逆数の和の逆数
result = 1 / np.sum(1.0 / A)

# 結果を出力
print(result)
