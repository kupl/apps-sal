import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    n, x, d = MI()
    if d == 0:
        if x == 0:
            print(1)
        else:
            print(n + 1)
        return
    if d < 0:
        d, x = -d, -x
    g = gcd(d, abs(x))
    d, x = d // g, x // g
    kk = list(range(n + 1))
    kk.sort(key=lambda k: (k * x % d, k))
    ans = 0
    pmd = -1
    pl, pr = 1, 0
    for k in kk:
        l = (k * x + (k - 1) * k // 2 * d) // d
        r = (k * x + (2 * n - k - 1) * k // 2 * d) // d
        md = x * k % d
        if md == pmd and l <= pr and pl <= r:
            pl, pr = min(pl, l), max(pr, r)
        else:
            ans += pr - pl + 1
            pl, pr = l, r
        pmd = md
    ans += pr - pl + 1
    print(ans)


main()
