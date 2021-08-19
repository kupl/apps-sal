import numpy as np

N = int(input())
A = np.array([int(x) for x in input().split()])

ans = 0
M = pow(10, 9) + 7
for i in range(100):
    one = int(np.sum((A >> i) & 1))
    zero = N - one
    ans += (one * zero) * pow(2, i, M)
    ans %= M
    # print(one,zero)
print(ans)
