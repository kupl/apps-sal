import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
#mod = 998244353
INF = 10**18
eps = 10**-7

N = int(input())
divisors = []
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        divisors.append(i)
        if i != N // i:
            divisors.append(N // i)

divisors.sort()
m = len(divisors)

if m % 2 == 0:
    print(divisors[m // 2] + divisors[m // 2 - 1] - 2)
else:
    print(divisors[m // 2] * 2 - 2)
