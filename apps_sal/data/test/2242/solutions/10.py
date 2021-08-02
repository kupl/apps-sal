from collections import Counter
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    s = input()
    n = len(s)

    amari = [0] * n
    ketaamari = 1
    t = 0
    for i1 in range(n):
        t = (t + ketaamari * int(s[-i1 - 1])) % 2019
        amari[-i1 - 1] = t
        ketaamari = (ketaamari * 10) % 2019
    amari.append(0)
    ac = Counter(amari)
    r = 0
    for v in ac.values():
        r += v * (v - 1) // 2
    print(r)


def __starting_point():
    main()


__starting_point()
