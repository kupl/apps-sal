import math as m
r = 0
for _ in range(int(input())):
    (k, a) = [int(x) for x in input().split()]
    e = 0
    v = 1
    while v < a:
        v *= 4
        e += 1
    if e + k > r:
        r = e + k
    if k + 1 > r:
        r = k + 1
print(r)
