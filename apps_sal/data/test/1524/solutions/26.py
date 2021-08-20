from itertools import groupby


def rfe_tuple(S):
    grouped = groupby(S)
    res = []
    for (k, v) in grouped:
        res.append((k, str(len(list(v)))))
    return res


def resolve():
    s = input()
    ls = rfe_tuple(s)
    ans = [0] * len(s)
    n = 0
    for (lr, i) in ls:
        i = int(i)
        if lr == 'R':
            n += i
            ans[n - 1] += i - i // 2
            ans[n] += i // 2
        else:
            ans[n - 1] += i // 2
            ans[n] += i - i // 2
            n += i
    print(*ans)


resolve()
