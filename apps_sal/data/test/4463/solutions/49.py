s = list(input())
t = list(input())

ss = sorted(s)
tt = sorted(t, reverse=True)

sa = ''.join(ss)
ta = ''.join(tt)

if sa < ta:
    print('Yes')
else:
    print('No')
