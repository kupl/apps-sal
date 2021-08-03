import math
import copy


def prime_factorize(n):
    a = [n]
    for i in range(2, math.floor(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            if n // i != i:
                a.append(n // i)
    return a


N = int(input())
prime_n = prime_factorize(N)
prime_n_1 = prime_factorize(N - 1)

ans = 0
for i in prime_n:
    n = copy.deepcopy(N)
    while (n % i) == 0:
        n = n // i
    if (n % i) == 1:
        ans += 1
ans += len(prime_n_1)
if N > 2:
    print(ans)
else:
    print(1)
