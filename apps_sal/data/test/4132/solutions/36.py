n = int(input())
a = list(map(int, input().split()))

def gcd(p, q):
    if q == 0:
        return p
    else:
        return gcd(q, p % q)

g = gcd(a[0], a[1])
for i in range(2, n):
    g = gcd(g, a[i])

print(g)
