n = int(input())
a = [int(i) for i in input().split()]
otrmax = -10 ** 4 - 1
polmin = 10 ** 4 + 1
sm = 0
for i in a:
    if i < 0:
        if i > otrmax and i % 2 == 1:
            otrmax = i
    else:
        if i < polmin and i % 2 == 1:
            polmin = i
        sm += i
if sm % 2 == 0:
    vrs = []
    if polmin != 10 ^ 4 + 1:
        vrs.append(sm - polmin)
    if otrmax != -10 ^ 4 - 1:
        vrs.append(sm + otrmax)
    print(max(vrs))
else:
    print(sm)
