S = input()
year = S[:4]
month = S[5:7]
day = S[8:10]
if int(year) < 2019:
    print('Heisei')
elif int(year) == 2019 and int(month) < 5 and (int(day) <= 30):
    print('Heisei')
else:
    print('TBD')
