def isTria(a,b,c,d,e,f):
    if abs(a*d-b*c+c*f-d*e+e*b-a*f) == 0:
        return 0
    else:
        return 1

def length(a,b,c,d):
    return (d-b)**2+(c-a)**2

ax,ay,bx,by,cx,cy=list(map(int,input().split()))
if not isTria(ax,ay,bx,by,cx,cy):
    print('No')
else:
    if length(ax,ay,bx,by) == length(bx,by,cx,cy):
        print('Yes')
    else:
        print('No')

