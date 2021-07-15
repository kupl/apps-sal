import numpy as np

# N,Aを取得
N = int(input())
A = np.array(list(map(int,input().split())))

# 逆数の和を取得する
result = 1 / np.sum(1 / A)

print(result)
