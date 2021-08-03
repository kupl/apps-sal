import math


def calc_base(k):
    base = k
    for i in range(1, k):
        base += 9 * i * (10 ** (i - 1))
    return base


def global_length(k):
    base = calc_base(k)
    d = 10 ** k - 10 ** (k - 1)
    if d % 2 == 0:
        return d * base + k * (d - 1) * (d // 2)
    return d * base + k * (d - 1) // 2 * d


def global_offset(k):
    offset = 0
    for i in range(1, k + 1):
        offset += global_length(i)
    return offset


def local_offset(k, l, base):
    return l * base + (k * l * (l - 1)) // 2


def bs_long(n):
    l, r = -1, 10
    while r - l > 1:
        m = (r + l) // 2
        s = global_offset(m)
        if n - s <= 0:
            r = m
        else:
            l = m
    if l < 0:
        return r
    return l


def bs_short(pos, base, k):
    l, r = -1, 10 ** k - 10 ** (k - 1)
    while r - l > 1:
        m = (r + l) // 2
        lb = local_offset(k, m, base)
        if pos - lb <= 0:
            r = m
        else:
            l = m
    return l


def digit_offset(number):
    k = int(math.log10(number))
    res = 0
    for i in range(k):
        res += int((i + 1) * 10 ** i)
    res *= 9
    res += (number - 10 ** k + 1) * (k + 1)
    return res - k


def bs_digit(k, x, base, n):
    l, r = 0, 10 ** k + x + 1
    while r - l > 1:
        m = (r + l) // 2
        lb = digit_offset(m)
        if n < lb:
            r = m
        else:
            l = m
    num = r if l < 1 else l
    n -= digit_offset(num)
    s = str(num)
    return s[n]


def solve(n):
    k = bs_long(n)
    n -= global_offset(k)
    base = calc_base(k + 1)
    d = bs_short(n, base, k + 1)
    n -= local_offset(k + 1, d, base)
    return bs_digit(k + 1, d, base, n)


def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = solve(n)
        print(a)


main()
