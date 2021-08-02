import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

# 総和は一定なので高橋君が何点(?)とるかの問題に置き換えられる
# d=0かつx=0のときは1、x!=0ならn+1で確定
# d,xと-d,-xは同値なので、dを正にすることで増加数列で考える
# d,xを同じ数で割っても答えは変わらないので、互いに素にする


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
    #print(x, d)
    # aをk個選ぶと和sはs=k*x+c*dで、cは最小で0からk-1の和
    # 最大でn-kからn-1の和
    # kを固定するとs//dは1ずつの単調増加なので、最小と最大で個数が分かる
    # sはs mod d = x*k mod dが同じなので、それで分類する
    kk = list(range(n + 1))
    kk.sort(key=lambda k: (k * x % d, k))
    # print(kk)
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
        #print(k, l, r, pl, pr, ans)
    ans += pr - pl + 1
    print(ans)


main()
