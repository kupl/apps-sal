from datetime import datetime
S = input()
s = datetime.strptime(S, '%Y/%m/%d')
str_std = '2019/04/30'
std = datetime.strptime(str_std, '%Y/%m/%d')
if s <= std:
    print('Heisei')
else:
    print('TBD')
