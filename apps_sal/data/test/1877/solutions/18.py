n = int(input())
s = input()
x = y = 0
p = 0
l = 'X'
lx = ly = -1
for c in s:
    if c == 'U':
        y += 1
    elif c == 'R':
        x += 1
    if lx == ly and l == c:
        p += 1
    l = c
    lx = x
    ly = y
print(p)
