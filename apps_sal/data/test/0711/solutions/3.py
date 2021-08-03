from collections import defaultdict
N, M = map(int, input().split())
count = defaultdict(int)
p = 2
while p <= 10**4.5 + 5:
    if M % p == 0:
        count[p] += 1
        M //= p
    else:
        p += 1
if M > 1:
    count[M] += 1


def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result


ans = 1
mod = 10**9 + 7
for i in count.keys():
    ans *= cmb(N - 1 + count[i], count[i])
    ans %= mod
print(ans)
