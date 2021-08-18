s = input()
if len(s) % 2:
    print(-1)
    return
x = 0
y = 0
for i in s:
    if i == 'L':
        x -= 1
    if i == 'R':
        x += 1
    if i == 'U':
        y += 1
    if i == 'D':
        y -= 1
x = abs(x)
y = abs(y)
print(x // 2 + y // 2 + max(x % 2, y % 2))
