from collections import defaultdict

N = int(input())

def factorize(N):
    factors = defaultdict(int)
    i = 2
    while i * i <= N:
        factor = 0
        while N % i == 0:
            N //= i
            factor += 1
        if factor > 0:
            factors[i] = factor
        i += 1
    if N > 1:
        factors[N] = 1
    return factors

def to_cnt(n):
    i = 0
    while n >= i+1:
        n-=(i+1)
        i += 1
    return i

ans = 0
for _, n in factorize(N).items():
    ans += to_cnt(n)
print(ans)
