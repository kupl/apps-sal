import numpy as np
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
mod = 10 ** 9 + 7
N = int(input())
A = np.array(list(map(int, input().split())))
ans = 0
for n in range(len(bin(max(A)))):
    num_1 = np.count_nonzero(A >> n & 1)
    num_0 = N - num_1
    mul = num_1 * num_0
    ans += 2 ** n * mul % mod
ans %= mod
print(ans)
