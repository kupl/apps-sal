s = input()
k = 0
s1 = ''
s2 = ['', '', '']
for a in s:
    if a == 'a' or a == 'e' or a == 'i' or (a == 'o') or (a == 'u'):
        s1 += a
        k = 0
    elif k + 1 == 3:
        s2[2] = a
        if s2[0] != s2[1] or s2[0] != s2[2]:
            s1 = s1 + ' ' + a
            k = 1
            s2[0] = a
        else:
            k = 2
            s1 += a
    else:
        s2[k] = a
        k += 1
        s1 += a
print(s1)
