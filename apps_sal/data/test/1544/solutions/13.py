def C(n,m):
    if m > n:
        return 0
    elif m == n:
        return 1
    elif m == 1:
        return n

    a = 1
    b = 1
    for i in range(1,m+1):
        a *= n+1-i
        b *= i
    return a//b

def __starting_point():

    n = int(input())

    a = C(n,1) + 4*C(n,2) + 6*C(n,3) + 4*C(n,4) + C(n,5)
    b = C(n,1) + 2*C(n,2) + C(n,3)

    print(a*b)
__starting_point()
