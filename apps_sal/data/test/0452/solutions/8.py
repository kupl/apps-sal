3

p, q = tuple(map(int, input().strip().split()))
n = int(input().strip())
a = list(map(int, input().strip().split()))
a.reverse()

def gcd(a, b):
    while a:
        a, b = b % a, a
    return b

g = gcd(p, q)
p, q = p // g, q // g

u, v = 0, 1;

for i in a:
    v, u = v * i + u, v
    g = gcd(u, v)
    u, v = u // g, v // g
if p == v and q == u:
    print("YES")
else:
    print("NO")

