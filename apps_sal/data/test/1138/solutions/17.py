s = input()
x, y = 0, 0
for ch in s:
    if ch == 'L':
        x = x - 1
    elif ch == 'R':
        x = x + 1
    elif ch == 'U':
        y = y - 1
    elif ch == 'D':
        y = y + 1
x = abs(x)
y = abs(y)
if x % 2 == y % 2:
    steps = x // 2 + y // 2
    if x % 2 == 1:
        steps = steps + 1
else:
    steps = -1
print(steps)
