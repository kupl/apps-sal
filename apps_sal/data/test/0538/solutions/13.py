import re
x = re.sub('0*$', '', input())
if x == x[::-1]:
    print('YES')
else:
    print('NO')
