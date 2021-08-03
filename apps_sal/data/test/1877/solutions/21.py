n = int(input())
s = input()
cnt = 0
p = True
x = 0
y = 0
for i in s:
    if not (x == 0 and y == 0):
        if p and x == y and i == 'R':
            cnt += 1
            p = False
        elif not p and x == y and i == 'U':
            cnt += 1
            p = True
    elif i == 'R':
        p = False
    else:
        p = True

    if i == 'R':
        x += 1
    if i == 'U':
        y += 1
print(cnt)
