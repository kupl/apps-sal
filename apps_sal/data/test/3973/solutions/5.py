import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def main():
    n, m = MI()
    aa = LI1()
    pp = [0] * (m + 1)
    qq = [0] * (m + 1)

    for a0, a1 in zip(aa, aa[1:]):
        if a0 < a1:
            pp[a0 + 1] += -1
            pp[a1 + 1] += 1
            qq[0] += a1 - a0
            qq[a0 + 1] += a0 + 1
            qq[a1 + 1] += -a0 - 1
        else:
            pp[0] += -1
            pp[a1 + 1] += 1
            pp[a0 + 1] += -1
            qq[0] += a1 + 1
            qq[a1 + 1] += m - a0 - 1
            qq[a0 + 1] += a0 + 1
    for i in range(1, m):
        pp[i] += pp[i - 1]
        qq[i] += qq[i - 1]
    ans = min(pp[i] * i + qq[i] for i in range(m))
    print(ans)


main()
