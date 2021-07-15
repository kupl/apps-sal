import numpy as np

n = int(input())
arr = np.array([int(i) for i in input().split()])
mod = 10 ** 9 + 7
s = 0

for i in range(60):
    c1 = np.count_nonzero(arr & 1) # 自分がnp.sumを利用したがどうしても正解になれなかった。なぜ？
    s += 2 ** i * c1 * (n - c1)
    arr >>= 1

print(s % mod)
