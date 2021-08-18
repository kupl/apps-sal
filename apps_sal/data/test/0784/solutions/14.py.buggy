rez = 'NO'
ms = []


def gen(a, b, mas):
    nonlocal rez, ms
    if a == b:
        rez = 'YES'
        ms = mas[:]
    elif a < b:
        gen(a * 2, b, mas + [a * 2])
        gen(a * 10 + 1, b, mas + [a * 10 + 1])


a, b = list(map(int, input().split()))
gen(a, b, [a])
if rez == 'YES':
    print(rez)
    print(len(ms))
    print(*ms)
else:
    print(rez)
