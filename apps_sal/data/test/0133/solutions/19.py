import sys
readline = sys.stdin.readline
mod = 10**9 + 7

N, M = map(int, readline().split())

x = pow(2, M, mod)
print(pow(x - 1, N, mod))
