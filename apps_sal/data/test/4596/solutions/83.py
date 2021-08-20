import sys


def iimr():
    return map(int, sys.stdin.readline().rstrip().split())


readline = sys.stdin.readline


def debug(*x):
    print(*x, file=sys.stderr)


class atcoder:

    def __init__(s):
        f = open(0)
        s.N = int(f.readline())
        s.A = list(map(int, f.readline().split()))

    def çözmek(s):
        res = []
        res.append(s.関数(s.N, s.A))
        print(*res)

    def 関数(self, n, a):
        guusuu = True
        cnt = 0
        while guusuu:
            for i in range(n):
                if a[i] % 2 != 0:
                    guusuu = False
                    break
                else:
                    a[i] /= 2
            if guusuu:
                cnt += 1
        return cnt


def __starting_point():
    ima = atcoder()
    ima.çözmek()


__starting_point()
