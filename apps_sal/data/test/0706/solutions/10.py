A, B, M = 0, 0, 10**9 + 7

def GP(A,n):
    if n == 0:
        return 1
    if A == 1:
        return (n * A) % M
    res = (pow(A,n,M)-1) * pow(A-1,M-2,M)
    return res % M

def f(n,x):
    res = pow(A,n,M) * x + B * GP(A,n)
    return res % M

def g(n,x):
    if n == 0:
        return x
    elif n == 1:
        return (A*x + B) % M
    return f(n,x) % M

A, B, n, x = list(map(int,input().split()))
print(g(n,x))

