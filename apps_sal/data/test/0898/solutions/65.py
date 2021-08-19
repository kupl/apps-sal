# author:  Taichicchi
# created: 11.10.2020 20:56:53

import sys


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N, M = list(map(int, input().split()))

i = 1
ans = 1
d_ls = make_divisors(M)
for i in d_ls:
    if i * N > M:
        break

    if (M - N * i) % i == 0:
        ans = i
    i += 1

print(ans)
