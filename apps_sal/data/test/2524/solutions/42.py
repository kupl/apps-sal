import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))
ans = 0
mod = 10 ** 9 + 7
for i in range(60):
    cnt = np.count_nonzero(A & 1)
    ans += (N - cnt) * cnt * 2 ** i
    ans %= mod
    A >>= 1
print(ans)
