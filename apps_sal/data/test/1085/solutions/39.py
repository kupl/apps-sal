import sys
n = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


sys.setrecursionlimit(10**7)


def func(N, d):
    if d == 1:
        return False
    while N > 1:
        if N % d == 0:
            N //= d
        else:
            if (N - 1) % d == 0:
                N = 1
            else:
                N = 0
    return True if N == 1 else False


ans = len(set(make_divisors(n - 1))) - 1
l = set(make_divisors(n))
for li in l:
    if func(n, li):
        ans += 1
print(ans)
