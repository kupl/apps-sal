s = input()
a = s.replace(';', ',').split(',')
(c, d) = ([], [])
for elem in a:
    if elem.isdigit() and (elem[0] != '0' or len(elem) == 1):
        c.append(elem)
    else:
        d.append(elem)
if len(c) == 0:
    print('-')
    print('"' + ','.join(d) + '"')
elif len(d) == 0:
    print('"' + ','.join(c) + '"')
    print('-')
else:
    print('"' + ','.join(c) + '"')
    print('"' + ','.join(d) + '"')
