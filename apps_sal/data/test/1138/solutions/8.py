commands = input()

nl = commands.count('L')
nr = commands.count('R')
nu = commands.count('U')
nd = commands.count('D')

if len(commands) % 2 != 0:
    print(-1)
else:
    dh = abs(nl - nr)
    dv = abs(nu - nd)
    if dh + dv == 0:
        print(0)
    elif dh % 2 == 0:
        print(dh // 2 + dv // 2)
    else:
        if dh < dv:
            dh, dv = dv, dh
        print((dh - 1) // 2 + (dv - 1) // 2 + 1)
