from sys import stdout
n = int(input())
s = [int(i) for i in input().split()]
a = s[0]
b = -1
c = -1
for i in s[1:]:
    if i != a and i != b and (i != c):
        if b < 0:
            b = i
        elif c < 0:
            c = i
        else:
            print('NO')
            break
else:
    if c == -1:
        print('YES')
    else:
        r = (max(a, b, c) - min(a, b, c)) / 2 + min(a, b, c)
        if a == r or b == r or c == r:
            print('YES')
        else:
            print('NO')
