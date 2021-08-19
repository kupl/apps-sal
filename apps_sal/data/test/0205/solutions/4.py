"""input
5 2
5 10
6 9
38 11
"""
(n, b) = map(int, input().split())
pm = 1
k = 0
i = 2
ans = float('inf')


def calc(n, b, k):
    res = 0
    t = pm
    while t <= n:
        res += n // t
        t *= pm
    return res // k


while i * i <= b:
    if b % i == 0:
        pm = i
        k = 0
        while b % i == 0:
            b //= i
            k += 1
        ans = min(ans, calc(n, b, k))
    i += 1
if b > 1:
    pm = b
    k = 1
    ans = min(ans, calc(n, b, k))
print(ans)
