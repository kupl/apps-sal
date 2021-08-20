for _ in range(int(input())):
    (l, r) = map(int, input().split())
    if l <= r // 2:
        print('NO')
    else:
        print('YES')
