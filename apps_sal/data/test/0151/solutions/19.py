s = input()
op = []
dl = len(s)
i = 2
gl = {'a', 'e', 'i', 'o', 'u'}
l = -1
while i < dl:
    if s[i - 2] not in gl and s[i - 1] not in gl and s[i] not in gl and s[i - 2:i + 1] != s[i - 2] * 3:
        if l == -1:
            l = i - 2
    elif l != -1:
        op.append(str(l) + '-' + str(i - 1))
        l = -1
    i += 1
else:
    if l != -1:
        op.append(str(l) + '-' + str(i - 1))
dlo = len(op)
for i in range(dlo - 1, -1, -1):
    l = int(op[i][:op[i].find('-')])
    r = int(op[i][op[i].find('-') + 1:])
    st = s[l:r + 1]
    dl = len(st)
    st1 = ''
    for j in range(0, dl, 2):
        st1 += st[j]
        if j < dl - 1:
            st1 += st[j + 1]
        if j < dl - 2:
            st1 += ' '
    s = s[:l] + st1 + s[r + 1:]
print(s)
