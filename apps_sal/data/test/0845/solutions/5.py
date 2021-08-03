d = input().strip()
s = input().strip()
if d == 'L':
    l = 1
else:
    l = -1
c1 = 'qwertyuiop'
c2 = 'asdfghjkl;'
c3 = 'zxcvbnm,./'
for i in s:
    if i in c1:
        print(c1[c1.find(i) + l], end='')
    if i in c2:
        print(c2[c2.find(i) + l], end='')
    if i in c3:
        print(c3[c3.find(i) + l], end='')
