import sys

def solve():
    a,b, = rv()
    awesome = min(a, b)
    a -= awesome
    b -= awesome
    ok = (a + b) // 2
    print(awesome, ok)



def prt(l): return print(' '.join(l))
def rs(): return map(str, input().split())
def rv(): return map(int, input().split())
def rl(n): return [list(map(int, input().split())) for _ in range(n)]  
if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
solve()
