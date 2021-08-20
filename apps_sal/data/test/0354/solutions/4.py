s = input()
t = input()
v = 'aeiou'
ok = len(s) == len(t)
if ok:
    for i in range(len(s)):
        isv1 = s[i] in v
        isv2 = t[i] in v
        ok &= isv1 and isv2 or (not isv1 and (not isv2))
if ok:
    print('Yes')
else:
    print('No')
