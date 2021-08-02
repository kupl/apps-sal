import sys


def get_primes(n: int):
    from itertools import chain
    from array import array
    primes = {2, 3}
    is_prime = (array('b', (0, 0, 1, 1, 0, 1, 0))
                + array('b', (1, 0, 0, 0, 1,0 ))*((n-1)//6))

    for i in chain.from_iterable((list(range(5, n + 1, 6)), list(range(7, n + 1, 6)))):
        if is_prime[i]:
            primes.add(i)
            for j in range(i * 3, n + 1, i * 2):
                is_prime[j] = 0

    return is_prime, primes


n, k = list(map(int, input().split()))
cards = list(map(int, input().split()))
_, primes = get_primes(32000)

div, div_cnt = [], []
for p in primes:
    if k % p == 0:
        div.append(p)
        div_cnt.append(0)
        while k % p == 0:
            div_cnt[-1] += 1
            k //= p
if k > 1:
    div.append(k)
    div_cnt.append(1)

m = len(div)
acc = [[0] * m for _ in range(n + 1)]

for i, x in enumerate(cards, start=1):
    for j in range(m):
        acc[i][j] += acc[i - 1][j]
        while x % div[j] == 0:
            acc[i][j] += 1
            x //= div[j]

ans = 0
j = 0
for i in range(n):
    j = max(j, i + 1)
    while j <= n and any(acc[j][k] - acc[i][k] < div_cnt[k] for k in range(m)):
        j += 1
    if j > n:
        break
    ans += n - j + 1

print(ans)
