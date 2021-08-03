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
    p, f = MI()
    cs, cw = MI()
    s, w = MI()
    if s > w:
        s, w = w, s
        cs, cw = cw, cs
    ans = 0
    for i in range(cs + 1):
        if i * s > p:
            break
        pw = (p - i * s) // w
        fs = min(cs - i, f // s)
        fw = min((f - fs * s) // w, cw - pw)
        cur = i + pw + fs + fw
        ans = max(ans, cur)
    print(ans)
