O = list(input())
E = list(input())

res = []

if len(O) - len(E) == 0:
    for i, j in zip(O, E):
        res.append(i)
        res.append(j)
else:
    E.append('')
    for i, j in zip(O, E):
        res.append(i)
        res.append(j)
    res.pop(-1)

pw = ''.join(res)
print(pw)
