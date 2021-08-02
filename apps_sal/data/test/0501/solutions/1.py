mod = 10**9 + 7

l, r = [int(i) for i in input().split()]


def calc(x):
    cur = 1
    a = []
    b = []
    move = 0
    su = 0
    while su <= x:
        if su + cur > x:
            break
        if move == 0:
            a.append(cur)
        else:
            b.append(cur)
        su += cur
        cur *= 2
        move ^= 1
    if su + cur > x:
        if move == 0:
            a.append(x - su)
        else:
            b.append(x - su)

    return sum(a), sum(b)


def tot(x):  # total sum of nums till x nums in list
    odds, evens = calc(x)
    ans = 0
    ans += ((odds % mod) * (odds % mod)) % mod
    ans += (((evens % mod) * (evens % mod)) % mod + evens) % mod
    return ans % mod


print((tot(r) - tot(l - 1)) % mod)
