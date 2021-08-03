import sys

sys.setrecursionlimit(10 ** 5)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


for _ in range(II()):
    s = SI()
    x = II()
    n = len(s)
    ans = [1] * n
    for i, c in enumerate(s):
        if c == "0":
            if i - x >= 0:
                ans[i - x] = 0
            if i + x < n:
                ans[i + x] = 0

    def ok():
        for i in range(n):
            if s[i] == "1":
                flag = 0
                if i - x >= 0:
                    flag |= ans[i - x]
                if i + x < n:
                    flag |= ans[i + x]
                if flag == 0:
                    return False
        return True

    if ok():
        print(*ans, sep="")
    else:
        print(-1)
