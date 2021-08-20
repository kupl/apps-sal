s = input()
s = s.replace('eraser', '#')
s = s.replace('erase', '#')
s = s.replace('dreamer', '#')
s = s.replace('dream', '#')
f = 0
for i in s:
    if i != '#':
        f = 1
        break
if f == 0:
    print('YES')
else:
    print('NO')
