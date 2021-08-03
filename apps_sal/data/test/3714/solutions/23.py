from math import gcd


def main():
    bb = [-1] * int(input())
    aa = [int(s) - 1 for s in input().split()]
    for b, a in enumerate(aa):
        if bb[a] != -1:
            print(-1)
            return
        bb[a] = b
    cc = set()
    for a, b in enumerate(bb):
        if b != -1:
            c = 0
            while bb[a] != -1:
                bb[a] = -1
                c += 1
                a = aa[a]
        cc.add(c)
    r = 1
    for c in cc:
        c //= 2 - c % 2
        r = r * c // gcd(r, c)
    print(r)


def __starting_point():
    main()


__starting_point()
