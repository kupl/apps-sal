a, b = input(), input()
dict = {}
d = []
for x in list(input()):
    if x in '0123456789':
        d.append(x)
    elif x == x.lower():
        d.append(b[a.index(x)])
    elif x == x.upper():
        d.append(b[a.index(x.lower())].upper())
print(''.join(d))
