import re
a, b = input().split()
s = input()
if re.match(r'\d{' + a + '}-\d{' + b + '}', s):
    print('Yes')
else:
    print('No')
