import math

la = int(input())
a = list(map(int, input().split()))

lb = int(input())
b = list(map(int, input().split()))

xa = 0
xb = 0

suma = 0
sumb = 0

result = 0
while (xa < la or sumb < suma) and  (xb < lb or suma < sumb):
    if suma == sumb:
        suma += a[xa]
        sumb += b[xb]
        xa += 1
        xb += 1
        result += 1

    elif suma > sumb:
        sumb += b[xb]
        xb += 1

    elif suma < sumb:
        suma += a[xa]
        xa += 1

if xa == la and xb == lb and suma == sumb:
    print(result)
else:
    print(-1)

