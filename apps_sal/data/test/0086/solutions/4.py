(xp, yp, xv, yv) = list(map(int, input().split()))
if xv >= xp and yv >= yp:
    print('Polycarp')
elif yv >= yp + xp:
    print('Polycarp')
elif xv >= xp + yp:
    print('Polycarp')
else:
    print('Vasiliy')
