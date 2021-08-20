a = input()
a = a.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
if len(a) == 0:
    print('YES')
else:
    print('NO')
