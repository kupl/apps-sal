x = input()
mode = 0
count = 0
for num in x.split(' '):
    if num == '5':
        mode += 1
    elif num == '7':
        mode += 4
    count += 1
if mode == 6 and count == 3:
    print('YES')
else:
    print('NO')
