s = input().replace(';', ',').split(',')
(a, b) = ([], [])
for i in s:
    if i.isdigit() and str(int(i)) == i:
        a.append(i)
    else:
        b.append(i)
if a:
    print('"{}"'.format(','.join(a)))
else:
    print('-')
if b:
    print('"{}"'.format(','.join(b)))
else:
    print('-')
