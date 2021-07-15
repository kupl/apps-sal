y, m, d = map(int,input().split('/'))
if y>2019:
    print('TBD')
elif y==2019 and m>4:
    print('TBD')
elif m==4 and d==31:
    print('TBD')
else:
    print('Heisei')
