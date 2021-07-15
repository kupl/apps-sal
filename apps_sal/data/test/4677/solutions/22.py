s = list(input())
li = []
for i in s:
    if i == '0':
        li.append('0')
    elif i == '1':
        li.append('1')
    elif i == 'B':
        if li == []:
            pass
        else:
            li.pop(-1)
print(''.join(li))
