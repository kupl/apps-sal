def solve(ls):
    import math
    (x, y, *ls) = ls
    z = x + y
    s = 0
    for a in ls:
        s ^= a
    if z - s < 0 or (z - s) % 2 == 1:
        return -1
    t = (z - s) // 2
    s_t = s & t
    if s_t > 0 or t > x:
        return -1
    a = t
    b = t
    first_set = math.floor(math.log2(s + 1))
    for i in range(first_set + 1)[::-1]:
        k = 1 << i
        if s & k:
            if a | k <= x:
                a = a | k
            else:
                b = b | k
    if a == 0:
        return -1
    return x - a


def main(istr, ostr):
    n = int(istr.readline().strip())
    ls = list(map(int, istr.readline().strip().split()))
    result = solve(ls)
    print(result, file=ostr)


def __starting_point():
    import sys
    main(sys.stdin, sys.stdout)


__starting_point()
