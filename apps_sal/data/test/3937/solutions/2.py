def gcd(a, b):
    if a < b:
        c = b
        b = a
        a = c
    while b != 0:
        t = b
        b = a % b
        a = t
    return int(a)


def extendedEuclides(a, b):
    xx = y = 0
    yy = x = 1
    while b != 0:
        q = int(a / b)
        t = b
        b = a % b
        a = t
        t = xx
        xx = x - q * xx
        x = t
        t = yy
        yy = y - q * yy
        y = t
    return [a, x, y]


def chineseRemainder(x, y, a, b):
    [d, s, t] = extendedEuclides(x, y)
    if(a % d != b % d):
        return [0, -1]
    return [int(((s * b * x + t * a * y) % (x * y)) / d), x * y / d]


[n, m, k] = input().split(' ')
n = eval(n)
m = eval(m)
k = eval(k)
arr = list(map(int, input().split(' ')))
I = 1
for el in arr:
    I = I * (el / gcd(I, el))
    if I > n:
        break
if I == 1:
    print("YES")
elif I > n:
    print("NO")
else:
    can = 1
    auxI = I
    fat = []
    occur = []
    for i in range(2, 1010000):
        if auxI % i == 0:
            v = 1
            while auxI % i == 0:
                v = v * i
                fat.append(v)
                occur.append(-1)
                auxI = int(auxI / i)
    if auxI > 1:
        fat.append(auxI)
        occur.append(-1)
    for i, x in enumerate(fat):
        for j in range(0, min(k, x)):
            if(gcd(arr[j], x) == x):
                occur[i] = j
        if occur[i] == -1:
            can = 0
    for i, x in enumerate(fat):
        for j in range(0, k):
            if ((gcd(arr[j], x) != x and j % x == occur[i]) or (gcd(arr[j], x) == x and j % x != occur[i])):
                can = 0
    I = 1
    J = 1
    lrem = 0
    for i, x in enumerate(fat):
        rem = (x - occur[i]) % x
        g = gcd(I, x)
        auxI = I * int(x / g)
        xxx = chineseRemainder(I, x, lrem % I, rem)
        lrem = xxx[0]
        I = auxI
        # print(lrem,rem,x,I)
    if lrem == 0:
        lrem = I
    if int(lrem) > m - k + 1:
        can = 0
    if can == 0:
        print('NO')
    else:
        print('YES')

# 1491583330722
