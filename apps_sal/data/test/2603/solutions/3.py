for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = a.copy()
    b.sort()
    impflag = 0
    arr = []
    val = min(a)
    for i in range(n):
        if a[i] != b[i]:
            arr.append(b[i])
    for i in arr:
        if i%val != 0:
            impflag = 1
            break
    if impflag == 1:
        print('NO')
    else:
        print('YES')

