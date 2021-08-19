n = int(input())
s = input()
vals = [0] * 10
for c in s:
    if c == 'L':
        free = vals.index(0)
        vals[free] = 1
    elif c == 'R':
        free = 9 - vals[::-1].index(0)
        vals[free] = 1
    else:
        cleared = int(c)
        vals[cleared] = 0
print(''.join(map(str, vals)))
