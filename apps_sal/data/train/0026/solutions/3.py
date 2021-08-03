t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a == 2 and b == 2:
        print('YES')
    elif a == 1:
        print('YES')
    elif b == 1:
        print('YES')
    else:
        print('NO')
