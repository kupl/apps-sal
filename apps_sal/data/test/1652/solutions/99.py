s = input()
s = s.replace('eraser', '#')
s = s.replace('erase', '#')
s = s.replace('dreamer', '#')
s = s.replace('dream', '#')
f = 1
for it in s:
    if it != '#':
        f = 0
        break
if f == 1:
    print('YES')
else:
    print('NO')
