n = int(input())

f, s, pts = [], [], 0
for i in range(n):
    pts = int(input())
    if (pts > 0):
        f.append(pts)
    else:
        s.append(-pts)

fs, ss = sum(f), sum(s)
fl, sl = len(f), len(s)

if (fs != ss):
    print('first' if fs > ss else 'second')
else:
    sm1won = False

    for i in range(min(fl, sl)):
        if (f[i] != s[i]):
            sm1won = True
            print('first' if f[i] > s[i] else 'second')
            break

    if (not sm1won):
        if (fl != sl):
            print('first' if fl > sl else 'second')
        else:
            print('first' if pts > 0 else 'second')
