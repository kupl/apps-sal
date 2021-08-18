import math
a1, b1, a2, b2, l, r = list(map(int, input().split()))
if b1 < l:
    b1 = (b1 - l) % a1 + l
if b2 < l:
    b2 = (b2 - l) % a2 + l
c = a1 // math.gcd(a1, a2) * a2
m = min(1 + r, c + max(b1, b2))
while b1 != b2 and m > b1:
    if b1 < b2:
        b1 = (b1 - b2) % a1 + b2
    else:
        b2 = (b2 - b1) % a2 + b1
print((m > b1) * (1 + (r - b1) // c))
