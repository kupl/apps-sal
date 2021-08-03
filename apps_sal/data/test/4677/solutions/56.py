s = input()
l = []
for i in range(len(s)):
    if s[i] == '0':
        l.append('0')
    elif s[i] == '1':
        l.append('1')
    else:
        if l == []:
            continue
        else:
            del l[-1]
print((''.join(l)))
