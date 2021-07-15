import re

s = input()
s = re.split(',|;', s)
a = []
b = []
for i in s:
    try:
        if str(int(i)) == i:
            a.append(i)
        else:
            b.append(i)
    except ValueError:
        b.append(i)
if len(a) == 0:
    print('-')
else:
    print("\"{}".format(a[0]), end='')
    for i in a[1:]:
        print(',{}'.format(i), end='')
    print('"')
if len(b) == 0:
    print('-')
else:
    print("\"{}".format(b[0]), end='')
    for i in b[1:]:
        print(',{}'.format(i), end='')
    print('"')
