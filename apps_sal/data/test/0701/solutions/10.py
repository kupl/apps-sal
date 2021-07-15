s = input().strip()
r = input().strip()
sd = dict()
rd = dict()
for k in s:
    if k in sd:
        sd[k] += 1
    else:
        sd[k] = 1
for k in r:
    if k in rd:
        rd[k] += 1
    else:
        rd[k] = 1

can = True
for k in r:
    if not (k in sd) or rd[k] > sd[k]:
        can = False
if not can:
    print('need tree')
else:
    can = True
    for k in s:
        if not (k in rd) or rd[k] != sd[k]:
            can = False
    if can:
        print('array')
    else:
        ind = 0
        for i in range(len(s)):
            if s[i] == r[ind] and ind < len(r)-1:
                ind += 1
        if ind == len(r)-1:
            print('automaton')
        else:
            print('both')

