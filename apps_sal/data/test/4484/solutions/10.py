n, m = list(map(int, input().split()))

p = 10**9 + 7


def ka(t):
    an = 1
    for i in range(2, t + 1):
        an = (an * i) % p
    return an


if n == m + 1 or n == m - 1:
    print(((ka(n) * ka(m)) % p))
elif n == m:
    print(((ka(n) * ka(m) * 2) % p))
else:
    print((0))
