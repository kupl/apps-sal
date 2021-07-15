from collections import defaultdict


def factorize(n: int) -> dict:
    f = defaultdict(int)
    while n % 2 == 0:
        f[2] += 1
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            f[p] += 1
            n //= p
        p += 2
    if n != 1:
        f[n] += 1
    return f


n = int(input())
ans = 1
for i in range(1, n + 1):
    f_ans = factorize(ans)
    f_i = factorize(i)

    for k, v in list(f_i.items()):
        if f_ans[k] < v:
            ans *= pow(k, v - f_ans[k])
ans += 1
print(ans)

