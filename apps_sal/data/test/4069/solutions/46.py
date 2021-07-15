X,K,D = map(int,input().split())
ans = 0
if X == 0:
    if K % 2 == 0:
        ans = 0
    else:
        ans = D
if X > 0:
    if K*D <= X:
        ans = X - K*D
    else:
        n = X // D
        if X % D != 0:
            n += 1
        if (K - n) % 2 == 0:
            ans = abs(X-D*n)
        else:
            ans = abs(X-D*(n-1))
if X < 0:
    if K*D + X <= 0:
        ans = abs(K*D+X)
    else:
        n = -X // D
        if -X % D != 0:
            n += 1
        if (K-n) % 2 == 0:
            ans = abs(X+n*D)
        else:
            ans = abs(X+(n-1)*D)

print(ans)
