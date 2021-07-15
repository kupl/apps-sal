import re

a = input()
a = re.match(r'[a-z]', a)

if a is None:
    print('A')
else:
    print('a')
