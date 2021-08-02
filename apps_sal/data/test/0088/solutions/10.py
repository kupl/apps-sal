a, b = list(map(int, input().split()))


def cnt(x):
    l = x.bit_length()
    res = 0
    for di in range(l):
        s = (1 << (l - di + 1)) - 1
        for i in range(l - di):
            if (s ^ (1 << i)) <= x:
                res += 1
    return res


print(cnt(b) - cnt(a - 1))
