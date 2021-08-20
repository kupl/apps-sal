from datetime import *
(y1, m1, d1) = map(int, input().split('/'))
date1 = date(y1, m1, d1)
date2 = date(2019, 4, 30)
if date1 <= date2:
    print('Heisei')
else:
    print('TBD')
