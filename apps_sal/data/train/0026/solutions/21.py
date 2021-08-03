for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if a == 1 or b == 1:
        print('YES')
    elif a == b == 2:
        print('YES')
    else:
        print('NO')
