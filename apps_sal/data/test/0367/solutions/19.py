def solve(s):
    cnt = dict()
    for c in s:
        if c not in cnt:
            cnt[c] = 0
        cnt[c] += 1
    num_odd = 0
    odds = []
    for (k, v) in list(cnt.items()):
        if v % 2:
            num_odd += 1
            odds.append(k)
    odds.sort()
    for i in range(num_odd // 2):
        cnt[odds[i]] += 1
        cnt[odds[-i - 1]] -= 1
    if len(s) % 2 == 0:
        return create_palin(cnt)
    else:
        return create_palin_odd(cnt)


def create_palin(cnt):
    total = sum((v for (k, v) in list(cnt.items())))
    p = [None] * total
    lo = 0
    hi = total - 1
    for (k, v) in sorted(cnt.items()):
        while v > 0:
            p[lo] = k
            p[hi] = k
            lo += 1
            hi -= 1
            v -= 2
    return str.join('', p)


def create_palin_odd(cnt):
    total = sum((v for (k, v) in list(cnt.items())))
    odd = [k for (k, v) in list(cnt.items()) if v % 2 == 1][0]
    p = []
    for (k, v) in sorted(cnt.items()):
        how = v // 2
        p += [k] * (v // 2)
    p = p + [odd] + list(reversed(p))
    return str.join('', p)


def __starting_point():
    s = input()
    print(solve(s))


__starting_point()
