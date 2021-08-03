n = int(input())
s = list(input())
a, b = list(map(int, input().split()))
L = s.count('L')
U = s.count('U')
R = s.count('R')
D = s.count('D')
x = 0
y = 0
xmin = 0
ymin = 0
minn = 2 * n
while x + y < 2 * n:
    if abs(a - (R - L)) + abs(b - (U - D)) > y - x and y != n:
        i = s[y]
        if i == 'L':
            L -= 1
        elif i == 'R':
            R -= 1
        elif i == 'D':
            D -= 1
        elif i == 'U':
            U -= 1
        y += 1
    elif abs(a - (R - L)) + abs(b - (U - D)) <= y - x or y == n:
        if y - x < minn and abs(a - (R - L)) + abs(b - (U - D)) <= y - x:
            minn = y - x
        i = s[x]
        if i == 'L':
            L += 1
        elif i == 'R':
            R += 1
        elif i == 'D':
            D += 1
        elif i == 'U':
            U += 1
        x += 1


if abs(a) + abs(b) > len(s):
    print(-1)
elif (len(s) - (abs(a) + abs(b))) % 2 != 0:
    print(-1)
else:
    print(minn)
