n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if x - y == 1:
        print('NO')
    else:
        print('YES')
