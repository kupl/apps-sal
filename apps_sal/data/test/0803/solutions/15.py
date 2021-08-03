n = int(input())
s = input()
r = (n >> 1) - s.count('x')
c = abs(r)
print(c)
i = 0
if r > 0:
    while c:
        if s[i] == 'X':
            print('x', end='')
            c -= 1
        else:
            print(s[i], end='')
        i += 1
    print(s[i:])
elif r < 0:
    while c:
        if s[i] == 'x':
            print('X', end='')
            c -= 1
        else:
            print(s[i], end='')
        i += 1
    print(s[i:])
else:
    print(s)
