import re

input()

a, s = [int(x) for x in input().split()], ''
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        s += '1'
    elif a[i] == a[i - 1]:
        s += '2'
    else:
        s += '3'

pattern = re.compile('^1*2*3*$')
if pattern.match(s):
    print('YES')
else:
    print('NO')

