input = __import__('sys').stdin.readline
x = 0
y = 0
for _ in range(int(input())):
    a, b, c = map(str, input().split())
    b, c = int(b), int(c)
    if a == '+':
        x = max(x, min(b, c))
        y = max(y, max(b, c))
    else:
        if (b >= x and c >= y) or (c >= x and b >= y):
            print('YES')
        else:
            print('NO')
