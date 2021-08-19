(n, a, b) = list(map(int, input().split()))
c = 0
d = 0
x = list(map(int, input().split()))
for v in x:
    if v > 1:
        if b > 0:
            b -= 1
        else:
            d += 2
    elif a > 0:
        a -= 1
    elif b > 0:
        b -= 1
        c += 1
    elif c > 0:
        c -= 1
    else:
        d += 1
print(d)
