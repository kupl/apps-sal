import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N = I()
m,a,r,c,h = 0,0,0,0,0
for _ in range(N):
    s = S()
    x = s[0]
    if x == 'M':
        m += 1
    elif x == 'A':
        a += 1
    elif x == 'R':
        r += 1
    elif x == 'C':
        c += 1
    elif x == 'H':
        h += 1

print((m*a*(r+c+h)+m*r*(c+h)+m*c*h+a*r*(c+h)+a*c*h+r*c*h))

