l = input()
s = []
for i in l:
    if i == 'V':
        s.append(1)
    else:
        s.append(0)
ls = len(s)
i = 0
maxc = 0
c = 0
while i + 1 < ls:
    if s[i] == 1 and s[i + 1] == 0:
        c += 1
    i += 1
maxc = max(maxc, c)
j = 0
while j < ls:
    if s[j] == 1:
        s[j] = 0
    else:
        s[j] = 1
    i = 0
    c = 0
    while i + 1 < ls:
        if s[i] == 1 and s[i + 1] == 0:
            c += 1
        i += 1
    maxc = max(c, maxc)
    if s[j] == 1:
        s[j] = 0
    else:
        s[j] = 1
    j += 1
print(maxc)
