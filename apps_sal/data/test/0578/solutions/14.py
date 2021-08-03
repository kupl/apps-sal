a, deb = input().split('.')
d, b = deb.split('e')
b = int(b)
if b < len(d):
    number = "{}{}.{}".format(a, d[:b], d[b:])
    number = number.strip('0')
    if number[0] == '.':
        number = "0{}".format(number)
    if number[-1] == '.':
        number = number[:-1]
else:
    number = "{}{}{}".format(a, d, '0' * (b - len(d)))
    number = number.lstrip('0')
    if not number:
        number = '0'
print(number)
