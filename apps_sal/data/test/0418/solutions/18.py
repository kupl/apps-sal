n = int(input())
for _ in range(n):
    (_, x, y) = input().split()
    x = int(x)
    y = int(y)
    if x < y and x >= 2400:
        print('YES')
        break
else:
    print('NO')
