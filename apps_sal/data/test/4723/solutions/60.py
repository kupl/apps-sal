import copy
s = list(input())
t = list(input())
(t1, t2) = (copy.deepcopy(s), copy.deepcopy(s))
ok = []
ch = True
if ch:
    for i in range(len(s) - len(t) + 1):
        count = 0
        for j in range(len(t)):
            if s[i + j] == t[j] or s[i + j] == '?':
                count += 1
        if count == len(t):
            ok.append(i)
if len(ok) == 0:
    print('UNRESTORABLE')
    ch = False
else:
    for i in range(len(t)):
        t1[ok[0] + i] = t[i]
    for i in range(len(t)):
        t2[ok[-1] + i] = t[i]
if ch:
    for i in range(len(t1)):
        if t1[i] == '?':
            t1[i] = 'a'
        if t2[i] == '?':
            t2[i] = 'a'
    (an1, an2) = ('', '')
    for i in t1:
        an1 += i
    for i in t2:
        an2 += i
    print(min(an1, an2))
