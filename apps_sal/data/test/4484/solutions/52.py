(n, m) = list(map(int, input().split()))
mod = 10 ** 9 + 7


def permitation(x):
    res = 1
    for i in range(1, x + 1):
        res = res * i % mod
    return res


pn = permitation(n)
pm = permitation(m)
if n == m:
    res = pn * pm * 2 % mod
    print(res)
elif n == m - 1 or n == m + 1:
    res = pn * pm % mod
    print(res)
else:
    print(0)
