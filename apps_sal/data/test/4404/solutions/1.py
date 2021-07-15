from datetime import datetime

S = input()
heiei = datetime(2019, 4, 30)
date = datetime.strptime(S, '%Y/%m/%d')

if heiei >= date:
    print('Heisei')
else:
    print('TBD')
