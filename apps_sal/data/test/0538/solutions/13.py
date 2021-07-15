import re
x = re.sub(r'0*$', '', input())
if x == x[::-1]:
    print('YES')
else:
    print('NO')


