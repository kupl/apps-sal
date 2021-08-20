from math import sqrt


def divisors(n):
    divisors = []
    for i in range(1, int(sqrt(n)) + 1):
        (q, r) = divmod(n, i)
        if r == 0:
            divisors.append(i)
            if i != q:
                divisors.append(q)
    divisors.sort()
    return divisors


(n, m) = map(int, input().split())
ans = 1
for a in divisors(m)[1:]:
    if a * n <= m:
        ans = a
print(ans)
