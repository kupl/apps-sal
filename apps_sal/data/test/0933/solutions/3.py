s = input()
C = [0] * len(s)
ind = -1
x = True
for i in range(len(s)):
    if x:
        C[i] = 1
        y = True
        x = False
        ind += 1
        continue
    if y:
        if s[i] == s[ind]:
            C[i] = 1
            z = True
            y = False
            ind += 1
            continue
        else:
            C[i] = 1
            ind += 1
            continue
    if z:
        if s[i] == s[ind]:
            C[i] = 0
            z = True
            continue
        else:
            C[i] = 1
            z = False
            a = True
            ind2 = i
            continue
    if a:
        if s[i] == s[ind2]:
            C[i] = 0
            continue
        else:
            ind = i
            C[i] = 1
            a = False
            y = True
for i in range(len(s)):
    if C[i]:
        print(s[i], end='')
