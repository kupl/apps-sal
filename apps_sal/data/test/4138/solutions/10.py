q = int(input())

sum = [0] * 20
cnt = [0] * 20

for i in range(1, 20):
    ct = 9 * (10 ** (i - 1))
    cnt[i] = cnt[i - 1] + i * ct
    sum[i] = sum[i - 1] + cnt[i - 1] * ct + i * (1 + ct) * ct // 2


def check(x, k, i):
    return cnt[i - 1] * x + i * (1 + x) * x // 2 < k


def check2(x, k):
    l = 0
    for i in range(10, -1, -1):
        if x - 10 ** i >= 0:
            x -= (10 ** i) - 1
            l = i + 1
            break

    return cnt[l - 1] + l * x < k


def cal(x):
    for i in range(10, -1, -1):
        if x - 10 ** i >= 0:
            return i + 1
    return 1


def rv(x):
    c = []
    while x:
        c.append(x % 10)
        x //= 10
    c.append(0)
    c.reverse()
    return c


while q:
    k = int(input())
    i = 10
    while sum[i] > k:
        i -= 1
    k -= sum[i]
    i += 1

    l = 1
    r = 10 ** 10
    while l < r:
        m = (l + r) // 2
        if check(m, k, i):
            l = m + 1
        else:
            r = m
    l -= 1
    k -= cnt[i - 1] * l + i * (1 + l) * l // 2

    ll = 1
    rr = 10 ** 10

    while ll < rr:
        m = (ll + rr) // 2
        if check2(m, k):
            ll = m + 1
        else:
            rr = m
    ll -= 1
    k -= cnt[cal(ll) - 1] + cal(ll) * (ll - 10**(cal(ll) - 1) + 1)

    c = rv(ll + 1)
    print(c[k])

    q -= 1
