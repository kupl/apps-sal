s = input()
a = []
b = []
tmp = ''
for i in s:
    if i == ',' or i == ';':
        if len(tmp) > 0 and tmp.isdigit() and (len(tmp) == 1 or tmp[0] != '0'):
            a.append(tmp)
        else:
            b.append(tmp)
        tmp = ''
    else:
        tmp = tmp + i
if len(tmp) > 0 and tmp.isdigit() and (len(tmp) == 1 or tmp[0] != '0'):
    a.append(tmp)
else:
    b.append(tmp)
if len(a) > 0:
    print('"' + ','.join(a) + '"')
else:
    print('-')
if len(b) > 0:
    print('"' + ','.join(b) + '"')
else:
    print('-')
