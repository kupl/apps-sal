A,B,C,X,Y = map(int,input().split())
sumAB = A+B
if sumAB >= 2*C:
    minXY = min(X,Y)
    ans = min(X,Y)*2*C
    X -= minXY
    Y -= minXY
    if X != 0:
        ans += X*min(A,2*C)
    elif Y !=0:
        ans += Y*min(B,2*C)
    print(ans)

else:
    print(A*X+Y*B)
