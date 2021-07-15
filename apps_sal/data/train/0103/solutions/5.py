for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    arr = [[0] * m for i in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))
    a = 0
    for i in range(n):
        if sum(arr[i]) == 0:
            a += 1
    b = 0
    for j in range(m):
        cnt = 0
        for i in range(n):
            cnt += arr[i][j]
        if cnt == 0:
            b += 1
    if min(a, b) % 2 == 1:
        print('Ashish')
    else:
        print('Vivek')

