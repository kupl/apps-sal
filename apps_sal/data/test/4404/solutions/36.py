y, m, d = input().split('/')
t = int(y + m + d)
if t <= 20190430:
    print('Heisei')
else:
    print('TBD')
