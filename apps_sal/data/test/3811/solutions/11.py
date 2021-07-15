from math import gcd, sqrt
n = int(input())


def divsor(a):
    for i in range(2, int(sqrt(a)) + 1):
        if not a % i:
            return i
    return a


a, b = map(int, input().split())
if n == 1:
    print(a)
    return
for i in range(n - 1):
    c, d = map(int, input().split())
    a = gcd(c*d, a); b = gcd(c*d, b)

if a > 1:
    print(divsor(a))
elif b > 1:
    print(divsor(b))
else:
    print(-1)
