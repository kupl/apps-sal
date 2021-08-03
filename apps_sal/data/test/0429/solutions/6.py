s = input()
f = False
for i in range(len(s) - 25):
    subs = s[i:i + 26]
    q = False
    for j in subs:
        if j == '?':
            continue
        elif subs.count(j) > 1:
            q = True
            break
    if q:
        continue
    else:
        f = True
        u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for j in u:
            if j not in subs:
                subs = subs[:subs.find('?')] + j + subs[subs.find('?') + 1:]
        s = s[:i] + subs + s[i + 26:]
        break
if (f):
    s = s.replace('?', 'A')
    print(s)
else:
    print(-1)
