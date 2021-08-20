from math import ceil
(k, a, b, v) = list(map(int, input().split(' ')))
p = ceil(a / v)
cajas = 0
dcaja = k - 1
divs = b
for i in range(p):
    if dcaja == k - 1 or divs == 0:
        cajas += 1
        dcaja = 0
    else:
        dcaja += 1
        divs -= 1
print(cajas)
