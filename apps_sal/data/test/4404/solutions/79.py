y, m, d = map(str, input().split('/'))
ymd = int(y + m + d)
if ymd <= 20190430:
    print('Heisei')
else:
    print('TBD')
