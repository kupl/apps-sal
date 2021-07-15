

A, B, C, X, Y = list(map(int,input().split()))

ans = 0

ab_total =  (C*2) * max(X,Y)

if C*2 < A+B:
    ans += min(X,Y) * (C*2)
    if X > Y:
        ans += (X - Y) * A
    else:
        ans += (Y - X)  * B
else:
    ans = A*X + B*Y

if ab_total < ans:
    print(ab_total)
else:
    print(ans)

