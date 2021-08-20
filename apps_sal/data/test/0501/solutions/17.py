def calc_even(n):
    if n <= 1:
        return 0
    i = 1
    while 2 ** i <= n:
        i += 2
    i -= 2
    cnt = 2 * (2 ** i - 2 ** (i - 1) - 1) // 3
    if 2 ** i + 2 ** i - 1 < n:
        cnt += 2 ** i
    else:
        cnt += n - 2 ** i + 1
    return cnt * (cnt + 1)


def calc_odd(n):
    if n < 1:
        return 0
    i = 0
    while 2 ** i <= n:
        i += 2
    i -= 2
    cnt = (2 ** i - 1) // 3
    if 2 ** i + 2 ** i - 1 < n:
        cnt += 2 ** i
    else:
        cnt += n - 2 ** i + 1
    return cnt * cnt


(l, r) = [int(x) for x in input().split()]
ans = calc_odd(r) - calc_odd(l - 1) + calc_even(r) - calc_even(l - 1)
print(ans % 1000000007)
