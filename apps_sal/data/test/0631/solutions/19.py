for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if sum(arr) == m:
        print('YES')
    else:
        print('NO')
