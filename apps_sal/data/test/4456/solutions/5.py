import sys


def main():
    n, m = [int(x) for x in sys.stdin.readline().strip().split()]
    p = [int(x) for x in sys.stdin.readline().strip().split()]
    q = [int(x) for x in sys.stdin.readline().strip().split()]

    sp = set()
    hashp = 0
    sq = set()
    hashq = 0

    res = ['z' for _ in range(n)]
    x = 0

    for c1, c2 in zip(p, q):
        sp.add(c1)
        hashp += c1 * c1
        sq.add(c2)
        hashq += c2 * c2

        if hashp == hashq and sp == sq:
            c = chr(ord('a') + x)
            x += 1
            for pos in sp:
                res[pos - 1] = c

            if x == m:
                print('YES')
                print(''.join(res))
                return

            sp.clear()
            hashp = 0
            sq.clear()
            hashq = 0


    print('NO')


main()

