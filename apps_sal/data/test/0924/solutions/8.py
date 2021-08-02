from math import gcd

C = lambda x, y: (x + y - 1) // y

l0, r0, t0 = map(int, input().split())
l1, r1, t1 = map(int, input().split())
g = gcd(t0, t1)
c = [0] * 4

i = min((r1 - r0) // g, (l1 - l0) // g)
if i >= C(l1 - r0, g):
    c[0] = r0 - l1 + g * i + 1

i = min((r0 - r1) // g, (l0 - l1) // g)
if i >= C(l0 - r1, g):
    c[1] = r1 - l0 + g * i + 1

i = min((r1 - r0) // g, (r1 - l0) // g)
if i >= max(C(l1 - r0, g), C(l1 - l0, g)):
    c[2] = r0 - l0 + 1

i = min((r0 - r1) // g, (r0 - l1) // g)
if i >= max(C(l0 - r1, g), C(l0 - l1, g)):
    c[3] = r1 - l1 + 1

# print(c)
print(max(c))
