s = input()
c0 = c1 = 0
d0 = []
for c in s:
    if c == '0': c0 += 1
    elif c == '1': c1 += 1
    else:
        d0.append(c0)
        c0 = 0
d0.append(c0)
res = []
for i in range(len(d0)):
    for j in range(d0[i]):
        res.append('0')
    if i == 0:
        for j in range(c1):
            res.append('1')
    if i < len(d0) - 1:
        res.append('2')
print(''.join(res))
