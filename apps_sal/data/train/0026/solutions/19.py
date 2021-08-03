for _ in range(int(input())):
    a, b = map(int, input().split())
    if min(a, b) == 1:
        print('YES')
    elif a == 2 and b == 2:
        print('YES')
    else:
        print('NO')
