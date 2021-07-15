import sys

def solve():
    n, = rv()
    h, = rl(1)
    maxsofar = 0
    res = [0] * n
    for i in range(n - 1, -1, -1):
        if h[i] <= maxsofar:
            res[i] = maxsofar - h[i] + 1
        else:
            maxsofar = h[i]
    prt(res)





def prt(l): return print(' '.join(map(str, l)))
def rs(): return map(str, input().split())
def rv(): return map(int, input().split())
def rl(n): return [list(map(int, input().split())) for _ in range(n)]  
if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
solve()
