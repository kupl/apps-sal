from sys import stdin, stdout
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split()))
    arr = sorted(arr)
    flg = 0
    for i in range(1, n):
        if arr[i] - arr[i - 1] > 1:
            flg = 1
            break
    if flg:
        print('NO')
    else:
        print('YES')
