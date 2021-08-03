from sys import stdin
x, y = 0, 0
for _ in range(int(input())):
    a, i, j = (o for o in stdin.readline().split())
    i, j = int(i), int(j)
    if a == '+':
        x = max(x, min(i, j))
        y = max(y, max(i, j))
    else:
        if (x <= i and y <= j) or (x <= j and y <= i):
            print("YES")
        else:
            print('NO')
