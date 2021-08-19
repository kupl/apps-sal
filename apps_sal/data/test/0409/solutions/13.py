import copy
si = list(input())
s = copy.deepcopy(si)
c1 = 0
i = 0
while i < len(s) - 1:
    if s[i:i + 2] == ['A', 'B']:
        s[i] = '.'
        s[i + 1] = '.'
        c1 = 1
        break
    i += 1
c2 = 0
i = 0
while i < len(s) - 1:
    if s[i:i + 2] == ['B', 'A']:
        s[i] = '.'
        s[i + 1] = '.'
        c2 = 1
        break
    i += 1
if c1 and c2:
    c3 = 1
else:
    c3 = 0
s = copy.deepcopy(si)
c2 = 0
i = 0
while i < len(s) - 1:
    if s[i:i + 2] == ['B', 'A']:
        s[i] = '.'
        s[i + 1] = '.'
        c2 = 1
        break
    i += 1
c1 = 0
i = 0
while i < len(s) - 1:
    if s[i:i + 2] == ['A', 'B']:
        s[i] = '.'
        s[i + 1] = '.'
        c1 = 1
        break
    i += 1
if c1 and c2 or c3:
    print('YES')
else:
    print('NO')
