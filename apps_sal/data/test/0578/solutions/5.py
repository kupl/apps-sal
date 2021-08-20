from decimal import *
getcontext().prec = 128
xs = input()
xs = [x for x in xs.split('e')]
a = Decimal(xs[0])
b = 10 ** int(xs[1])
s = str(a * b)
i = len(s) - 1
while i > 0 and s[i] == '0':
    i = i - 1
if s[i] == '.':
    i = i - 1
print(s[:i + 1])
