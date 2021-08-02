a, b, c, d, e = input(), input(), [0], 0, 0
for i in range(len(b)):
    d += int(b[i])
    c.append(d)
for i in range(len(a)):
    nOO = c[len(b) - (len(a) - i) + 1] - c[i]
    nOZ = len(b) - len(a) + 1 - nOO
    if a[i] == '0':
        e += nOO
    else:
        e += nOZ
print(e)
