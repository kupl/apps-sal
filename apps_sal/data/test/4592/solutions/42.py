from math import sqrt
n = int(input())
d = {}
mod = 10**9 + 7
for i in range(1, n):
    m = i + 1

    for j in range(2, int(sqrt(i + 1)) + 1):
        if m % j == 0:
            while m % j == 0:
                d[j] = d.get(j, 0) + 1
                m //= j
    if m > 1:
        d[m] = d.get(m, 0) + 1

ans = 1
for i in d:
    ans *= d[i] + 1
    ans %= mod
print(ans)
