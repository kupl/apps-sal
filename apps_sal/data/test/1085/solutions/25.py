"""
0, K, 2K, 3K, 4K, ... = N-1 のとき, 答え.
"""


def makediv(n):
    (lower_divisors, upper_divisors) = ([], [])
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


n = int(input())
ans = 0
themakedivlist = makediv(n - 1)
for i in themakedivlist:
    if i >= 2:
        ans += 1
k = makediv(n)
k.remove(1)
for i in k:
    tmpn = n
    while True:
        if tmpn == 1:
            ans += 1
            break
        elif tmpn % i == 0:
            tmpn //= i
        elif (tmpn - 1) % i == 0:
            ans += 1
            break
        else:
            break
print(ans)
