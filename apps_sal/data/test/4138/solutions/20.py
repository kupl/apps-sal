def sum_first(k):
    return (k + 1) * k // 2


def sum_seq_len(k):
    res = 0
    x = 1
    while k >= x:
        res += sum_first(k - (x - 1))
        x *= 10
    return res


def seq_len(k):
    res = 0
    x = 1
    while k >= x:
        res += k - (x - 1)
        x *= 10
    return res


def brut_ssl(k):
    res = 0
    for i in range(1, k + 1):
        for j in range(1, i + 1):
            res += len(str(j))
    return res


def brut_sl(k):
    res = 0
    for i in range(1, k + 1):
        res += len(str(i))
    return res


def binsrch(a, b, x, f):
    if a == b - 1:
        return a
    mid = (a + b) // 2
    if f(mid) < x:
        return binsrch(mid, b, x, f)
    else:
        return binsrch(a, mid, x, f)


def test(x):
    pref_seq_cnt = binsrch(0, 100 * x, x, sum_seq_len)
    seq_l = x - sum_seq_len(pref_seq_cnt)
    big = binsrch(0, seq_l, seq_l, seq_len)
    ind = seq_l - seq_len(big)
    return str(big + 1)[ind - 1]


def __starting_point():
    T = int(input())
    for _ in range(T):
        x = int(input())
        print(test(x))


__starting_point()
