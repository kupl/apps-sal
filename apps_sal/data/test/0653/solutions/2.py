n = int(input())
l = [0] * 10
for c in input():
    if c == 'L':
        l[l.index(0)] = 1
    elif c == 'R':
        l.reverse()
        l[l.index(0)] = 1
        l.reverse()
    else:
        l[int(c)] = 0
print(*l, sep='')
