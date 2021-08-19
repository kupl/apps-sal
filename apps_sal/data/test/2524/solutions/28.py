import numpy as np

mod = 10 ** 9 + 7

N = int(input())
A = np.array(list(map(int, input().split())))


tmp = 0
for n in range(len(bin(max(A))) - 2):   # 最大桁数は、最も大きい数値の2進数の桁数
    num_1 = np.count_nonzero((A >> n) & 1)   # 1の数をカウント
    num_0 = N - num_1                      # 0の数をカウント
    mul = num_1 * num_0   # 0 XOR 1の回数
    tmp += ((2 ** n) * mul) % mod
ans = tmp % mod
print(ans)
