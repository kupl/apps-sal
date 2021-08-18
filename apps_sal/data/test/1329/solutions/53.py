def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())

d = {}
for i in range(2, n + 1):
    p = prime_factorize(i)
    for cp in p:
        if cp in d:
            d[cp] += 1
        else:
            d[cp] = 1

cnt = {75: 0, 25: 0, 15: 0, 5: 0, 3: 0}
for i in d:
    for j in cnt:
        if d[i] >= j - 1:
            cnt[j] += 1
ans = cnt[75] + cnt[25] * (cnt[3] - 1) + cnt[15] * (cnt[5] - 1) + cnt[5] * (cnt[5] - 1) // 2 * (cnt[3] - 2)
print(ans)
