from math import factorial
import sys
input = sys.stdin.readline


def comb(a, d):
    return factorial(a) // factorial(b) // factorial(a - b)


mod = 10 ** 9 + 7
N = int(input())
C_input = list(map(int, input().split()))
C = sorted(C_input)
ans = 0
for (ind, s) in enumerate(C):
    ans += C[ind] * (N + 1 - ind)
    ans %= mod
print(int(ans * 2 ** (2 * N - 2)) % mod)
