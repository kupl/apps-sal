d = {}
s = input()
for l in s:
    if l not in d:
        d[l] = 0
    d[l] += 1
if len(d) > 4:
    print('No')
elif len(d) == 3:
    if len(s) > 3:
        print('Yes')
    else:
        print('No')
elif len(d) == 2:
    for k in d:
        if d[k] < 2:
            print('No')
            return
    print('Yes')
elif len(d) == 4:
    print('Yes')
else:
    print('No')
