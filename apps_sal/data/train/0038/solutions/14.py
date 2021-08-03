for case in range(int(input())):
    input()
    a = max(list(map(int, input().split())))
    b = max(list(map(int, input().split())))
    print('YES' if a > b else 'NO')
