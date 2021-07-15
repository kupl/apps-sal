x, y = list(map(int, input().split()))

def ncr(n, r, p):
    num = 1
    den = 1

    for i in range(r):
        num = (num*(n-i)) % p
        den = (den*(i+1)) % p

    return (num*pow(den, p-2, p)) % p

if (x+y)%3 == 0:
    n = (x+y)//3

    if not (n <= x <= 2*n):
        print(0)
    else:
        print(ncr(n, x-n, 1000000007))
else:
    print(0)
