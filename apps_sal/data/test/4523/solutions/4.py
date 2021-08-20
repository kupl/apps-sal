for _ in range(int(input())):
    am = int(input())
    arr = list(map(int, input().split()))
    fl = True
    arr.sort()
    for i in range(am - 1):
        if arr[i + 1] - arr[i] > 1:
            fl = False
            break
    if fl:
        print('YES')
    else:
        print('NO')
