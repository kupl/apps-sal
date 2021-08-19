s = input()
flag = False
ind = [0, 0, 0, 0, 0]
for i in range(len(s)):
    if s[i] == 'h':
        ind[0] = i + 1
        break
if ind[0]:
    for i in range(ind[0] - 1, len(s)):
        if s[i] == 'e':
            ind[1] = i + 1
            break
if ind[1]:
    for i in range(ind[1] - 1, len(s)):
        if s[i] == 'i':
            ind[2] = i + 1
            break
if ind[2]:
    for i in range(ind[2] - 1, len(s)):
        if s[i] == 'd':
            ind[3] = i + 1
            break
if ind[3]:
    for i in range(ind[3] - 1, len(s)):
        if s[i] == 'i':
            ind[4] = i + 1
            flag = True
            break
print('YES' if flag else 'NO')
