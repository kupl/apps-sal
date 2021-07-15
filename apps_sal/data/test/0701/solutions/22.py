s = input()
t = input()
np = 0
for c in s:
    if np < len(t) and c == t[np]:
        np += 1
if np == len(t):
    print('automaton')
else:
    ds = {}
    dt = {}
    for c in s:
        if c not in ds:
            ds[c] = 0
        ds[c] += 1
    for c in t:
        if c not in dt:
            dt[c] = 0
        dt[c] += 1
    flag = True
    for c in dt:
        if c not in ds or dt[c] > ds[c]:
            flag = False
    if flag:
        if len(s) == len(t):
            print('array')
        else:
            print('both')
    else:
        print('need tree')

