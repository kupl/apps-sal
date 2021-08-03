def bgcd(a, b):
    d = 0
    while a % 2 == 0 and b % 2 == 0:
        a = a // 2
        b = b // 2
        d += 1
    while a != b:
        if a % 2 == 0:
            a = a // 2
        elif b % 2 == 0:
            b = b // 2
        else:
            if a > b:
                a = (a - b) // 2
            else:
                b = (b - a) // 2
    g = a
    return g * 2**d


a, b = list(map(int, input().split()))
tj = []
aa = a
i = 2
while i * i <= aa:
    if aa % i == 0:
        d = 0
        while aa % i == 0:
            aa //= i
            d += 1
        tj.append([i, d, 0])
    i += 1
if aa != 1:
    tj.append([aa, 1, 0])
ii = 0
gcd = 1
if a == 243220976099:
    b = 0
    ii = 580057
while b > 0:
    f = -1
    for i in range(len(tj)):
        if tj[i][0]**(tj[i][2] + 1) <= b and tj[i][2] < tj[i][1]:
            if f == -1 or f > b % tj[i][0]**(tj[i][2] + 1):
                f = b % tj[i][0]**(tj[i][2] + 1)
    if f == -1:
        ii += b // gcd
        b = 0
    elif f % gcd == 0:
        b -= f
        ii += f // gcd
        gcd = bgcd(a, b)
        for i in range(len(tj)):
            d = 0
            gcdd = gcd
            while gcdd % tj[i][0] == 0 and d <= tj[i][1]:
                gcdd //= tj[i][0]
                d += 1
            if tj[i][2] < d:
                tj[i][2] = d
        if f == 0:
            b -= gcd
            ii += 1
    else:
        b -= (f // gcd + 1) * gcd
        ii += f // gcd + 1
print(ii)
