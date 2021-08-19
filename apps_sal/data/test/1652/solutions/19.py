s = str(input())
isYES = True
while len(s) > 0:
    if s[-5:] == 'dream':
        s = s[:-5]
    elif s[-7:] == 'dreamer':
        s = s[:-7]
    elif s[-5:] == 'erase':
        s = s[:-5]
    elif s[-6:] == 'eraser':
        s = s[:-6]
    else:
        isYES = False
        break
    # print(s)
if isYES:
    print('YES')
else:
    print('NO')
