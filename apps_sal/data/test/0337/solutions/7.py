w,h = list(map(int,input().split()))
u1,d1 = list(map(int,input().split()))
u2,d2 = list(map(int,input().split()))

while h > 0:
    w += h
    if h == d1:
        w -= u1
    if h == d2:
        w -= u2
    w = max( 0, w )
    h -= 1

print( w )

