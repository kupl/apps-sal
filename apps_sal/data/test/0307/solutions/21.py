def lmap(f, x):
    return list(map(f, x))


def read_ints():
    return lmap(int, input().strip().split())


def main():
    res = 0
    (a2, a3, a5, a6) = read_ints()
    n256 = min(a2, a5, a6)
    res += n256 * 256
    a2 -= n256
    a5 -= n256
    a6 -= n256
    n32 = min(a3, a2)
    res += n32 * 32
    return res


print(main())
