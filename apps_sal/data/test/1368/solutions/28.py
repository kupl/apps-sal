nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

N,A,B = map(int,input().split())
v = sorted(list(map(int,input().split())),reverse=True)

if len(set(v)) == 1:
    print(1)
    print(1125899906842623)
    return

m = sum(v[:A])/A
print(m)

if len(set(v[:A]))==1:
    ans = 0
    c = v.count(v[0])
    for i in range(A,B+1):
        if i <= c:
            ans += cmb(c,i)
    print(ans)
    return

mi = min(v[:A])
n = v[:A].count(mi)
m = v.count(mi)
print(cmb(m,n))
