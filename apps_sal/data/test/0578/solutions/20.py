from math import modf
s = input()
i = 0
while s[i] != 'e':
    i += 1
a = s[0:i]
b = int(s[i + 1:])
i = 0
while s[i] != '.':
    i += 1
a2 = a[i + 1:]
a = a[0:i]
i = 0
while b > 0 and i < len(a2):
    a += a2[i]
    i += 1
    b -= 1
if b > 0:
    while b > 0:
        a += '0'
        b -= 1
elif i < len(a2):
    a2 = a2[i:]
    a3 = ''
    i = len(a2) - 1
    k = 0
    while i > -1:
        if a2[i] != '0' and k == 0:
            k = 1
            a3 = a2[i] + a3
        elif k != 0:
            a3 = a2[i] + a3
        i -= 1
    if len(a3) != 0:
        a += '.'
        for i in range(len(a3)):
            a += a3[i]
print(a)
