S = input()
s = S.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
if s == '':
    print('YES')
else:
    print('NO')
