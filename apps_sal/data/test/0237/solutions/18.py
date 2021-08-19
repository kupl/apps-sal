import sys


def sum_(a):
    return max(0, a * (a + 1) // 2)


def check(a):
    if a * n <= m:
        return 1
    a -= 1
    ans = n
    t1 = a - k + 1
    if t1 >= 0:
        ans += sum_(a) - sum_(t1 - 1)
    else:
        ans += sum_(a)
    z = n - k + 1
    t2 = a - z + 1
    if t2 >= 0:
        ans += sum_(a - 1) - sum_(t2 - 1)
    else:
        ans += sum_(a - 1)
    return ans <= m


def bins():
    l = 1
    r = m + 1
    while l + 1 != r:
        m1 = (l + r) // 2
        if check(m1):
            l = m1
        else:
            r = m1
    print(l)


(n, m, k) = list(map(int, input().split()))
bins()
