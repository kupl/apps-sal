import datetime

s = input()

s_date = datetime.datetime.strptime(s, '%Y/%m/%d')

last_date = '2019/05/01'

t_date = datetime.datetime.strptime(last_date, '%Y/%m/%d')

if s_date < t_date:
    print('Heisei')

else:
    print('TBD')
