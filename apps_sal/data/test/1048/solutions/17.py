n = int(input())
commands = input()
left = 0
right = 0
up = 0
down = 0
for i in commands:
    if i == 'U':
        up += 1
    elif i == 'D':
        down += 1
    elif i == 'R':
        right += 1
    elif i == 'L':
        left += 1
    else:
        raise ValueError
print(2*min(right, left) + 2*min(up, down))

