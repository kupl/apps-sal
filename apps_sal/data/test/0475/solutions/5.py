P = 998244353
def C(n, k):
    nonlocal P
    k = min(k, n-k)
    p = 1
    for i in range(n, n-k, -1):
        p *= i
    for i in range(k, 0, -1):
        assert(p%i==0)
        p //= i
    return p%P

n, m, k = list(map(int, input().split()))

r = C(n-1, k)
r = (r*m)%P
for i in range(k):
    r = (r*(m-1))%P
print(r)


