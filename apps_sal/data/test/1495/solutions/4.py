from collections import Counter


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
        while mi != ma or not (mi & 1):
            mask &= mask << 1
            mi >>= 1
            ma >>= 1
    mask ^= (1 << le) - 1
    le, cnt = mask.bit_length(), Counter()
    for a, i in zip(aa, l):
        a &= mask
        if a:
            a = a.bit_length()
        cnt[i, a] += 1
    res = [0] * (le + 1)
    for (i, a), c in list(cnt.items()):
        if a:
            base, baseidx = (a - i) * c, le - a
        else:
            base, baseidx = 0, le - i
        j = base
        for i in range(baseidx - 1, -1, -1):
            j += c
            res[i] += j
        j = base
        for i in range(baseidx, le + 1):
            res[i] += j
            j += c
    print(min(res))


def __starting_point():
    main()




# Made By Mostafa_Khaled

__starting_point()
