s = input()
d = dict()
for si in s:
    if si not in list(d.keys()):
        d[si] = 1
    else:
        d[si] += 1

if len(d) != 2:
    print('No')
    return
else:
    for v in list(d.values()):
        if v != 2:
            print('No')
            return
print('Yes')

