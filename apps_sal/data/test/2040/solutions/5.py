def get_smallest(dig_sum):
    ret = str(dig_sum % 9) + '9' * (dig_sum // 9)
    return int(ret)


def f(n):
    ret = 0
    while n:
        ret += n % 10
        n //= 10
    return ret


def nx(n):
    s = str(n)
    sm = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] < '9' and sm > 0:
            return int(s[:i] + str(int(s[i]) + 1) + str(get_smallest(sm - 1)).zfill(len(s) - i - 1))
        sm += int(s[i])
    return int('1' + str(get_smallest(sm - 1)).zfill(len(s)))


def after(d, low):
    s = '0' * 600 + str(low)
    n = len(s)
    has = f(low)
    for i in range(n - 1, -1, -1):
        has -= int(s[i])
        for x in range(int(s[i]) + 1, 10):
            if s[i] < '9' and has + x <= d <= has + x + 9 * (n - i - 1):
                if i == n - 1:
                    return int(s[:i] + str(x))
                return int(s[:i] + str(x) + str(get_smallest(d - has - x)).zfill(n - i - 1))


n = int(input())
low = 0
for i in range(n):
    ds = int(input())
    cur = after(ds, low)
    print(cur)
    low = cur
