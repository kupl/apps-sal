import math
(n, m) = map(int, input().split())
znach = range(1, 200)
for i in range(m):
    (k, f) = map(int, input().split())
    if f == 1:
        a = range(math.ceil(k / f), 200)
    else:
        niz = math.ceil(k / f)
        verh = math.floor((k - 1) / (f - 1))
        a = range(niz, verh + 1)
    znach = list(set(a) & set(znach))
if len(znach) == 1:
    if n % znach[0] == 0:
        print(n // znach[0])
    else:
        print(n // znach[0] + 1)
else:
    a = []
    for i in range(len(znach)):
        if n % znach[i] == 0:
            a.append(n // znach[i])
        else:
            a.append(n // znach[i] + 1)
    a = list(set(a))
    if len(a) > 1:
        print(-1)
    else:
        print(a[0])
