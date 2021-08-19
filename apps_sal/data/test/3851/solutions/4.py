import math
(n, k) = [int(x) for x in input().split()]
(a, b) = [int(x) for x in input().split()]
c = n * k
r1 = (a + b) % c
r2 = (a - b) % c
r3 = (b - a) % c
r4 = (-a - b) % c
valid_jump = []
for x in range(0, n):
    valid_jump.append((x * k + r1) % c)
    valid_jump.append((x * k + r2) % c)
    valid_jump.append((x * k + r3) % c)
    valid_jump.append((x * k + r4) % c)
for i in range(0, len(valid_jump)):
    if valid_jump[i] == 0:
        valid_jump[i] = 1
    else:
        valid_jump[i] = int(c / math.gcd(c, valid_jump[i]))
g = valid_jump[0]
h = valid_jump[0]
for element in valid_jump:
    if element > g:
        g = element
    if element < h:
        h = element
print(h, g)
