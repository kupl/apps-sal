def main():
    input()
    aa = list(map(int, input().split()))
    le, l = max(aa).bit_length(), []
    for i, a in enumerate(aa):
        j = le - a.bit_length()
        aa[i] = a << j
        l.append(j)
    mi, ma = min(aa), max(aa)
    a = mask = (1 << le) - 1
    if mi == ma:
        while mi == mi & a:
            mask = a
            a &= a << 1
    else:
        while mi != ma:
            mask &= mask << 1
            mi >>= 1
            ma >>= 1
        while not (mi & 1):
            mask &= mask << 1
            mi >>= 1
    mask ^= (1 << le) - 1
    le = mask.bit_length() + 1
    res = [0] * le
    cache = {}
    for a, i in zip(aa, l):
        a &= mask
        if a:
            a = a.bit_length()
        tmp = cache.get((i, a))
        if tmp is None:
            cache[i, a] = tmp = [0] * le
            if a:
                base, baseidx = a - i, le - a - 1
            else:
                base, baseidx = 0, le - i - 1
            i, j = baseidx, base
            while i:
                i -= 1
                j += 1
                tmp[i] = j
            i, j = baseidx, base
            while i < le:
                tmp[i] = j
                i += 1
                j += 1
        for i, j in enumerate(tmp):
            res[i] += j
    print(min(res))


def __starting_point():
    main()

__starting_point()
