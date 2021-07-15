A, B, C, X, Y = list(map(int,input().split()))

min_p = 100000000000000
for c in range(0, max(X, Y)*2+1):
    a = X - int(c / 2)
    b = Y - int(c / 2)

    if a < 0 :
        a = 0
    if b < 0:
        b = 0

    p = A*a+B*b+C*c
    min_p = min(min_p, p)
print(min_p)

