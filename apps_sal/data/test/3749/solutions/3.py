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
    if a < b:
        a, b = b, a
    k = a.bit_length() - b.bit_length()
    return gcd(b, a ^ (b << k))


def main():
    md = 998244353
    n, x = input().split()
    x = int(x, 2)
    aa = [input() for _ in range(int(n))]
    aa = [int(a, 2) for a in aa]
    # bitを多項式の係数と考えて多項式のGCDを求める
    g = aa[0]
    for a in aa[1:]:
        g = gcd(g, a)
    # print(bin(g))
    # GCDの桁数以上は自由に決められるのでその分を答えに
    ans = x >> (g.bit_length() - 1)
    s = 0
    # GCDの桁数以上をxと同じにした場合にx以下になるようであればその分も足す
    while 1:
        k = (x ^ s).bit_length() - g.bit_length()
        # print(k,bin(x^s),bin(x),bin(s))
        if k < 0:
            break
        s ^= g << k
    if s <= x:
        ans += 1
    print(ans % md)


main()
