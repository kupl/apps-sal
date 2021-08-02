s = input()
x = 0
y = 0
for i in s:
    if i == 'U':
        y += 1
    elif i == 'D':
        y -= 1
    elif i == 'R':
        x += 1
    else:
        x -= 1
if (abs(x) + abs(y)) % 2 == 1:
    print(-1)
else:
    print(int((abs(x) + abs(y)) / 2))
