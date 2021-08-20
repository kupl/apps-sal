import math
(a, b) = map(int, input().split())


def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    if b == 0:
        return a
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


g = gcd(a, b)
x = g
s = set()
for i in range(2, int(math.sqrt(g)) + 1):
    while x % i == 0:
        s.add(i)
        x /= i
if x != 1:
    s.add(x)
print(len(s) + 1)
