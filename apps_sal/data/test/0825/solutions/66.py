from collections import Counter


def factor(n):
    p = []
    if n == 1:
        return p
    m = n
    i = 2
    while i * i <= n:
        while m % i == 0:
            m //= i
            p.append(i)
        i += 1
    if m > 1:
        p.append(m)
    return p


n = int(input())
p = Counter(factor(n))
ans = 0
for x in p.values():
    i = 1
    while x - i >= 0:
        x -= i
        i += 1
        ans += 1
print(ans)
