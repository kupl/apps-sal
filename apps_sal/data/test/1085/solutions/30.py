import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
INF = 10**18
eps = 10**-7

N = int(input())


def divisor(n):
    ass = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n // i)
    return ass


ans = len(divisor(N - 1)) - 1
b = divisor(N)
for bi in b:
    if bi == 1:
        continue
    a = N
    while a >= bi:
        if a % bi == 0:
            a = a // bi
        else:
            a = a % bi
    if a == 1:
        ans += 1
print(ans)
