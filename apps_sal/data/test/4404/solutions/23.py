s = input()
if int(s[:4]) < 2019:
    print('Heisei')
elif int(s[:4]) > 2019:
    print('TBD')
elif int(s[5:7]) <= 4:
    print('Heisei')
elif int(s[5:7]) > 4:
    print('TBD')
