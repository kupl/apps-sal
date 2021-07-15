import sys
def v():
    pt=[5,0,1,2]
    s=list(['0' if x=='g' else '1' for x in list(sys.stdin.readline().strip())])
    n=len(s)
    p=pt[n%4]
    for _ in range(n//4):p=(p<<4)+5
    ss=list(format(p,'b').zfill(n))
    res=0
    for a,b in zip(s,ss):
        d=int(b)-int(a)
        res = res if d==0 else res+d
    print(res)
def __starting_point():v()

__starting_point()
