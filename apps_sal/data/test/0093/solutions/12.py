per1 = input()
per2 = input()
per3 = input()
per4 = input()
s = []
s.append(per1[0])
s.append(per1[1])
s.append(per2[1])
s.append(per2[0])
for i in range(len(s)):
    if s[i] == 'X':
        s.pop(i)
        break
d = []
d.append(per3[0])
d.append(per3[1])
d.append(per4[1])
d.append(per4[0])
for i in range(len(d)):
    if d[i] == 'X':
        d.pop(i)
        break
per2 = False
for i in range(3):
    if s != d:
        t = d.pop(0)
        d.append(t)
    else:
        per2 = True
        break
if per2:
    print('YES')
else:
    print('NO')
