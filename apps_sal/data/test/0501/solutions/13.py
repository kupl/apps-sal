l, r = list(map(int, input().split()))

mod = 10**9 + 7


def f(l):
    left = 0
    c = 0
    while left < l:
        left += pow(2, c)
        c += 1

    extra = left - l
    ls = 0
    odd = 0
    eve = 0

    for i in range(c):
        if i % 2 == 0:
            odd += pow(2, i)
        else:
            eve += pow(2, i)
    temp = 0
    if c % 2 == 1:
        temp = (odd - extra) * (odd - extra) + eve * (eve + 1)
    else:
        temp = odd * odd + (eve - extra) * (eve + 1 - extra)

    return temp


print((f(r) - f(l - 1) + mod) % mod)
