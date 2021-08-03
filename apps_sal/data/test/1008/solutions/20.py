from fileinput import *

for line in input():
    if lineno() == 1:
        s = line.strip()
    if lineno() == 2:
        n = int(line.strip())

sl = len(s)
unit_length = sl // n

newlist = []

for i in range(n):
    newlist.append(s[i * unit_length:i * unit_length + unit_length])


def is_p(word):
    return word == word[::-1]


res = True
for word in newlist:
    if is_p(word):
        pass
    else:
        res = False
        break

if res and sl % n == 0:
    print('YES')
else:
    print('NO')
