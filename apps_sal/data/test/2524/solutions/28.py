import numpy as np

mod = 10 ** 9 + 7

N = int(input())
A = np.array(list(map(int, input().split())))


tmp = 0
for n in range(len(bin(max(A))) - 2):
    num_1 = np.count_nonzero((A >> n) & 1)
    num_0 = N - num_1
    mul = num_1 * num_0
    tmp += ((2 ** n) * mul) % mod
ans = tmp % mod
print(ans)
