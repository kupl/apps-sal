def way_cut(x1,y1,x2,y2):
    return (((x1-x2)**2+(y1-y2)**2)**0.5)
r,x,y,x1,y1 = list(map(int,input().split()))
z = way_cut(x,y,x1,y1)
if z % (2 * r) == 0:
    print(int(z // (2 * r)))
else:
    print(int(z // (2 * r))+1)

