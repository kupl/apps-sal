for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    flag = 0
    for i in range(n - 1):
        if arr[i + 1] - arr[i] > 1:
            flag = 1
            break
    if flag:
        print('NO')
    else:
        print('YES')
