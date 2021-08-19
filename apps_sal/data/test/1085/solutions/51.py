N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


ans = len(make_divisors(N - 1)) - 1


def check(n, x):
    while n % x == 0:
        n //= x
    return n % x == 1


for i in range(2, int(N ** 0.5) + 1):
    if N % i == 0:
        if check(N, i):
            ans += 1
ans += 1
print(ans)
