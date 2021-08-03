s = input()

if len(s) % 2 == 1:
    print(-1)
    return

horizontal = 0
vertical = 0

for k in s:
    if k == 'L':
        horizontal += 1
    elif k == 'R':
        horizontal -= 1
    elif k == 'U':
        vertical += 1
    elif k == 'D':
        vertical -= 1

horizontal = abs(horizontal)
vertical = abs(vertical)

print((horizontal + vertical) // 2)
