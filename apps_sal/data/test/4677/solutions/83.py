s = str(input())
l = []
for i in s:
    if i == '0' or i == '1':
        l.append(i)
    elif i == 'B' and len(l) != 0:
        l.pop(len(l) - 1)
print(*l, sep='')
