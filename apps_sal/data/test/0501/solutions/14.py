mod = 1000000007


def f(n):
    f = 1
    s = 2
    t = 1
    ret = 0
    cnt = 0
    p = 1
    while cnt + p <= n:
        cnt += p
        if t == 1:
            ret = (ret + (2 * f + (p - 1) * 2) * p // 2) % mod
            f += 2 * p
        else:
            ret = (ret + (2 * s + (p - 1) * 2) * p // 2) % mod
            s += 2 * p
        p *= 2
        t += 1
        if t > 2:
            t = 1
    if t == 1:
        ret = (ret + (2 * f + (n - cnt - 1) * 2) * (n - cnt) // 2) % mod
    else:
        ret = (ret + (2 * s + (n - cnt - 1) * 2) * (n - cnt) // 2) % mod
    return ret


(l, r) = list(map(int, input().split()))
print((f(r) - f(l - 1) + mod) % mod)
