import bisect


def enum_devisors(n):
    divisors = set([])
    for i in range(1, int(n**.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors


n, m = list(map(int, input().split()))
devisors = sorted(enum_devisors(m))
d = devisors[bisect.bisect_left(devisors, n)]
print(m // d)
