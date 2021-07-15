from decimal import Decimal, getcontext

getcontext().prec = 250
s = "{:.250f}".format(Decimal(input()))

if '.' in s:
    while s[-1] == '0':
        s = s[:-1]
    if s[-1] == '.':
        s = s[:-1]

print(s)

