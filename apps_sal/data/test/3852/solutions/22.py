n = int(input())

a = [int(x) for x in input().split()]

ma = max(a)
mi = min(a)

if(ma*mi < 0):
    print((2*n-1))
    if ma > -1*mi:
        for i in range(n):
            print((a.index(ma)+1, i+1))
        for i in range(n-1):
            print((i+1, i+2))
    else:
        for i in range(n):
            print((a.index(mi)+1, i+1))
        for i in range(n-1):
            print((n-i, n-i-1))
else:
    print((n-1))
    if(ma > 0):
        for i in range(n-1):
            print((i+1, i+2))
    else:
        for i in range(n-1):
            print((n-i, n-i-1))

