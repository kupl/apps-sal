str = input().replace(';', ',')
lst = str.split(',')


a = ''
b = ''
first_in_a = True
first_in_b = True
amount = 0

for item in lst:
    is_int = True
    for ch in item:
        if not (48 <= ord(ch) <= 57):
            is_int = False
            break
    if len(item) == 0:
        is_int = False
    if is_int:
        if (len(item) > 1) and (item[0] == '0'):
            is_int = False
    if is_int:
        if not first_in_a:
            a += ','
        else:
            first_in_a = False
        a += item
    else:
        if not first_in_b:
            b += ','
        else:
            first_in_b = False
        b += item
        amount += 1

if len(a) > 0:
    print('"%s"' % a)
else:
    print('-')
if amount > 0:
    print('"%s"' % b)
else:
    print('-')
