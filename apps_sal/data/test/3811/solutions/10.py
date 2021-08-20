from math import gcd, sqrt


def divsor(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


n = int(input())
(a, b) = map(int, input().split())
for i in range(n - 1):
    (c, d) = map(int, input().split())
    a = gcd(c * d, a)
    b = gcd(c * d, b)
if a != 1:
    print(divsor(a))
elif b != 1:
    print(divsor(b))
else:
    print(-1)
