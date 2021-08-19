string_list = input().split(sep='.')
integer = string_list[0].lstrip('0')
if len(string_list) == 1:
    fractional = ''
else:
    fractional = string_list[1].rstrip('0')
if integer:
    if fractional:
        a = '{}.{}{}'.format(integer[0], integer[1:], fractional)
    else:
        a = '{}.{}'.format(integer[0], integer[1:].rstrip('0'))
    d = len(integer) - 1
    if a[-1] == '.':
        a = a[:-1]
    if d > 0:
        print('E'.join((a, str(d))))
    else:
        print(a)
else:
    old_len = len(fractional)
    fractional = fractional.lstrip('0')
    zero_count = old_len - len(fractional)
    a = '{}.{}'.format(fractional[0], fractional[1:])
    d = -zero_count - 1
    if a[-1] == '.':
        a = a[:-1]
    print('E'.join((a, str(d))))
