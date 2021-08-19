import sys
(n, m) = map(int, sys.stdin.readline().split())
f = [1, 1]
mod = 1000000007
for i in range(100000):
    f.append(f[-1] + f[-2])
res = 2 * (f[n] + f[m] - 1)
res %= mod
print(res)
