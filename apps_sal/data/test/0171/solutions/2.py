import re
a1 = re.compile('[a-z]')
a2 = re.compile('[A-Z]')
a3 = re.compile('[0-9]')
s = input()
if len(s) >= 5:
    s = list(s)
    ar = [0, 0, 0]
    for i in s:
        if(a1.match(i) != None):
            ar[0] += 1
    for i in s:
        if(a2.match(i) != None):
            ar[1] += 1
    for i in s:
        if(a3.match(i) != None):
            ar[2] += 1
    if (ar[0] != 0 and ar[1] != 0 and ar[2] != 0):
        print('Correct')
    else:
        print('Too weak')
else:
    print('Too weak')
