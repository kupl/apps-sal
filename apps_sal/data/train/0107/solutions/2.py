import sys

t = int(input())

for i in range(t):
    a1, a2, a3, a4 = list(map(int, input().split()))

    neg = (a1 + a2) % 2 == 1

    large = (a1 == 0 and a4 == 0)
    small = (a2 == 0 and a3 == 0)

    r1, r2, r3, r4 = True, True, True, True
    if(neg):
        r3, r4 = False, False
    else:
        r1, r2 = False, False

    if large:
        r1, r4 = False, False

    if small:
        r2, r3 = False, False

    res = ''
    for j in [r1, r2, r3, r4]:
        if (j):
            res += 'Ya '
        else:
            res += 'Tidak '

    print(res[:-1])
