n, k = list(map(int, input().split()))

m = 1000000007

def ncr(n, r, p):
    num = 1
    den = 1

    for i in range(r):
        num = (num*(n-i)) % p
        den = (den*(i+1)) % p

    return (num*pow(den, p-2, p)) % p

def comb(n, k, lowerBound):
    if lowerBound == 0:
        return ncr(n+k-1, n, m)
    else:
        return comb(n-(k*lowerBound), k, 0)

for i in range(1, k+1):
    ans = comb(k, i, 1)
    red = n-k-(i-1)

    if red < 0:
        ans = 0
    else:
        ans *= comb(red, i+1, 0)

    print(ans%m)
