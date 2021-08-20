__author__ = 'hamed1soleimani'
lines = ['qwertyuiop', 'asdfghjkl;', 'zxcvbnm,./']
offset = input()
if offset == 'R':
    offset = -1
else:
    offset = 1
li = input()
ou = ''
for ch in li:
    for line in lines:
        i = line.find(ch)
        if i != -1:
            ou += line[i + offset]
print(ou)
