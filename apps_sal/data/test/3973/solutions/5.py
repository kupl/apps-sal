import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n, m = MI()
    # 明るさaは0-indexedにする
    aa = LI1()
    # 頂点xをお気に入りにしたときのスコアをpx+qで表す
    # imos法を使う
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

