n = int(input())
s = input()
count = 0
kindom = 0
x, y = 0, 0
for i in s:
    if i == 'U':
        y += 1
    elif i == 'R':
        x += 1
    if x > y:
        if kindom == 2:
            count += 1
        kindom = 1
    if x < y:
        if kindom == 1:
            count += 1
        kindom = 2
print(count)

