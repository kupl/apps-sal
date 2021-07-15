i=input;k = int(i());x, y = list(map(int, i().split()));x,y=x-y,x+y
def cc(x, xs):
    if abs(x-xs)<=2*k and abs(x-xs)%2==0:
        return 1,x+(k if abs(x+k-xs) <= abs(x-k-xs) else -k)
    return 0,xs+(k if x-xs>0 else -k)
if (k%2,x%2)==(0,1):
    print((-1))
else:
    rs = []
    xs, ys = 0, 0
    while True:
        if abs(x-xs) == k or abs(y-ys) == k:
            if abs(x-xs) <= k and abs(y-ys) <= k:
                rs+=["{} {}".format((x+y)//2,(y-x)//2)]
                break
        mm,ys=cc(y,ys)
        if mm:
            xs = xs+(k if x > xs else -k)
        else:
            mm, xs = cc(x, xs)
        rs+=["{} {}".format((xs+ys)//2,(ys-xs)//2)]
    print((len(rs)))
    print(("\n".join(rs)))

