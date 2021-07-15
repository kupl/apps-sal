n = int(input())
s = str(input())
sE = s.count('E')
sW = s.count('W')
l = []
e, w = 0, 0
for ch in s:
    if ch == 'E':
        e += 1
    else:
        w += 1
    m = (sE-e)+w
    l.append(sE-e+w-1 if ch == 'W' else sE-e+w)
print((min(l)))

