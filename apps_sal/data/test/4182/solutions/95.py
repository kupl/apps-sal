a,b,x,y = map(int, input().split())

xl = list(map(int, input().split()))
yl = list(map(int, input().split()))

xx = max(xl)
xx = max(xx,x)
yy = min(yl)
yy = min(yy,y)

if xx<yy:
    print("No War")

else:
    print("War")
