xp, yp, xv, yv = (int(x) for x in input().split())
if xp <= xv and yp <= yv:
    print('Polycarp')
    return
if xv <= xp and yv <= yp:
    print('Vasiliy')
    return
if xv > xp and yv < yp:
    if xv - xp >= yp:
        print('Polycarp')
    else:
        print('Vasiliy')
    return
if yv - yp >= xp:
    print('Polycarp')
else:
    print('Vasiliy')
