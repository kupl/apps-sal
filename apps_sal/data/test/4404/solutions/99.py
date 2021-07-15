s = input()
s_i = s[0:4] + s[5:7] + s[-2:]

if int(s_i) <= 20190430:
    print('Heisei')
else:
    print('TBD')
