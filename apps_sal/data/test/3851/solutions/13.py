import math

def gcdi(p, q):
    while q > 0:
        r = p % q
        p = q
        q = r
    return p

def gcd(p, q):
    p = abs(p)
    q = abs(q)
    return gcdi(max(p,q), min(p,q))

n, k = map(int, input().strip().split())
a, b = map(int, input().strip().split())

tests = [(a, b), (a, k-b), (k-a, b), (k-a, k-b)]
ansx = math.inf
ansy = -math.inf
for (aa, bb) in tests:
    d = bb-aa
    for i in range(n):
        l = i*k+d
        z = n*k/gcd(n*k,l)
        ansx = min(ansx, z)
        ansy = max(ansy, z)
print('%d %d' % (ansx, ansy))
