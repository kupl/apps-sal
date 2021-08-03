import sys

sys.setrecursionlimit(10 ** 5)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


for _ in range(II()):
    n = II()
    aa = LI1()
    cnt = [0] * n
    ans = 0
    for i, a in enumerate(aa):
        cur = 0
        for a2 in aa[i + 1:]:
            if a2 == a:
                ans += cur
            cur += cnt[a2]
        cnt[a] += 1
    print(ans)
