split_by_dot = input().split('.')
split_by_e = split_by_dot[1].split('e')
a = split_by_dot[0]
d = split_by_e[0]
b = int(split_by_e[1])
D = d.lstrip('0')
decimals = len(d)
if a == '0':
    if d == '0':
        print('0')
    elif b < decimals:
        integer_part = '0' if b == 0 else d[:b - 1].lstrip('0') + d[b - 1]
        decimal_part = d[b:]
        print(integer_part, '.', decimal_part, sep='')
    else:
        print(d.lstrip('0'), '0' * (b - decimals), sep='')
elif d == '0':
    print(a, '0' * b, sep='')
elif b < decimals:
    print(a, d[:b], '.', d[b:], sep='')
else:
    print(a, d, '0' * (b - decimals), sep='')
