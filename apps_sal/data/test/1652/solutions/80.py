s = str(input())
words = ['dream', 'erase', 'eraser', 'dreamer']
i = len(s)
while i > 0:
    if s[-5:] in words:
        s = s[:-5]
        i -= 5
    elif s[-6:] in words:
        s = s[:-6]
        i -= 6
    elif s[-7:] in words:
        s = s[:-7]
        i -= 7
    else:
        break
if i == 0:
    print('YES')
else:
    print('NO')
