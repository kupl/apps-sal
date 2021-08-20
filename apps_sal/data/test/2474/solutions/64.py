from sys import stdin
f_i = stdin
mod = 10 ** 9 + 7
N = int(f_i.readline())
C = map(int, f_i.readline().split())
C = sorted(C)
x = (C_i * i % mod for (i, C_i) in zip(range(N + 1, 1, -1), C))
ans = pow(4, N - 1, mod) * sum(x) % mod
print(ans)
