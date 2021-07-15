#より高速に
def pow(x, n ,p):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K = (x*K) % p
        x = (x*x) % p
        n //= 2

    return (K * x) % p




def cmb3(n,r,q):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)    
    s = 1
    for x in range(n,n-r,-1):
        s = (s*x) % q
    t = 1
    for x in range(1,r+1):
        t = (t*x) % q

    #割る数の剰余をどうするかが問題
    u = pow(t,q-2,q)
    return (u * s) % q
  
n,a,b = list(map(int,input().split()))
A = pow(2,n,10**9+7)

if a <= n:
  B = cmb3(n,a,10**9+7)
else:
  B = 0
if b <= n:
  C = cmb3(n,b,10**9+7)
else:
  C = 0

print(((A-B-C-1)%(10**9+7)))


