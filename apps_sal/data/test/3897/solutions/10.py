from collections import defaultdict
f = [1] * 15001
fi = [1] * 15001
a = 1
b = 1
m = 10**9 + 7
for i in range(1, 15001):
    a *= i
    b *= pow(i, m - 2, m)
    a %= m
    b %= m
    f[i] = a
    fi[i] = b
d = defaultdict(int)


def factorize(n):
    count = 0
    while ((n % 2 > 0) == False):

        n >>= 1
        count += 1
    if (count > 0):
        d[2] += count
    for i in range(3, int(n**0.5) + 1):
        count = 0
        while (n % i == 0):
            count += 1
            n = int(n / i)
        if (count > 0):
            d[i] += count
        i += 2

    if (n > 2):
        d[n] += 1


ans = 1
n = int(input())
l = list(map(int, input().split()))
for i in l:
    factorize(i)
for i in d:
    ans *= (f[d[i] + n - 1] * fi[n - 1] * fi[d[i]]) % m
    ans %= m
print(ans)
