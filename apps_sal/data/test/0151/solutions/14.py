s = input()
fl = False
l1 = ''
l2 = ''
l = 0
gl = {'a', 'e', 'i', 'o', 'u'}
for i in range(len(s)):
    if s[i] in gl:
        l1 = ''
        l2 = ''
    elif l2 == '':
        l2 = s[i]
        continue
    elif l1 == '':
        l1 = s[i]
        continue
    elif s[i] == l2 and s[i] == l1:
        continue
    else:
        print(s[l:i] + ' ', end='')
        l1 = ''
        l2 = s[i]
        l = i
print(s[l:])
