for i in range(int(input())):
    n, k1, k2 = list(map(int, input().split()))
    u = max(list(map(int, input().split())))
    v = max(list(map(int, input().split())))
    if u < v:
        print('NO')
    else:
        print('YES')

