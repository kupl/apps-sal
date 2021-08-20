(a, b, c) = map(int, input().split('/'))
if a > 2019:
    print('TBD')
elif a < 2019:
    print('Heisei')
elif b <= 4:
    print('Heisei')
else:
    print('TBD')
