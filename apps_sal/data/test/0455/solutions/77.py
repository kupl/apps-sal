import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n = ni()
xy = []
for _ in range(n):
    x,y = li()
    xy.append((x,y))
    
exist = True
    
eo = (xy[0][0]+xy[0][1]) % 2
for x,y in xy[1:]:
    if (x+y)%2 != eo:
        exist = False
    
if not exist:
    print(-1)
    
else:
    if eo == 1:
        arms = [2**i for i in range(40)]
        print(40)
        print(*arms[::-1])
        
    else:
        arms = [1] + [2**i for i in range(39)]
        print(40)
        print(*arms[::-1])
        
    for x,y in xy:
        u,v = x-y, x+y
        ucur, vcur = 0,0
        ans = ""
        for am in arms[::-1]:
            if ucur >= u and vcur >= v:
                ucur -= am
                vcur -= am
                ans += "L"
                
            elif ucur <= u and vcur <= v:
                ucur += am
                vcur += am
                ans += "R"
                
            elif ucur >= u and vcur <= v:
                ucur -= am
                vcur += am
                ans += "U"
                
            elif ucur <= u and vcur >= v:
                ucur += am
                vcur -= am
                ans += "D"
                
        print(ans)
