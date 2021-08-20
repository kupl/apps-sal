for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    np = False
    for i in range(n):
        if ar[i] - ar[i - 1] > 1:
            np = True
    if np:
        print('NO')
    else:
        print('YES')
