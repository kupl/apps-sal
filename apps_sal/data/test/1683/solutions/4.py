from collections import Counter

_MODER = 998244353


# split s
# def split_str(s):
#     return '0'.join(list(s)) + '0'

def solve(n, a):
    r = 0
    c = Counter()  # c[k]; number of elements whose length is k
    for e in a:
        c[len(str(e))] += 1

    for e in a:
        s = str(e)

        current_len = len(s)
        for k, v in list(c.items()):
            # s is a
            if k >= current_len:
                ns = '0'.join(list(s)) + '0'
            else:
                ns = s[:current_len - k] + '0'.join(list(s[current_len - k:])) + '0'
            r = (r + (int(ns) * v) % _MODER) % _MODER

            # s is b
            if k >= current_len - 1:
                ns = '0'.join(list(s))
            else:
                ns = s[:current_len - k - 1] + '0'.join(list(s[current_len - k - 1:]))
            r = (r + (int(ns) * v) % _MODER) % _MODER
    return r


n = int(input())
a = list(map(int, input().split()))

r = solve(n, a)
print(r)
