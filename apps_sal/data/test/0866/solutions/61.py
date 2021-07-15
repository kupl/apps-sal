mod = 10**9 + 7

def nCk(n,k,p):
    nonlocal mod
    k = min(k, n-k)
    
    X = 1
    for i in range(k):
        X = X * (n - i) % p
        X = X * pow(i + 1, p - 2, p) % p
    return X

X,Y = map(int, input().split())

ans = 0
if X <= 2*Y and Y <= 2*X and (X + Y) % 3 == 0:
    a = (2*Y-X) // 3
    b = (2*X-Y) // 3
    ans = nCk(a + b, b, mod)
print(ans)
