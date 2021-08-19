for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    prr = list(map(int, input().split()))
    for i in range(m):
        prr[i] -= 1
    temp = arr[:]
    temp.sort()
    cnt = 0
    f = 0
    prev = arr[:]
    while cnt < n ** 2:
        for i in range(m):
            (x, y) = (prr[i], prr[i] + 1)
            if arr[x] > arr[y]:
                (arr[x], arr[y]) = (arr[y], arr[x])
                cnt += 1
        if arr == temp:
            f = 1
            break
        if prev == arr:
            break
        prev = arr[:]
    if f == 1:
        print('YES')
    else:
        print('NO')
