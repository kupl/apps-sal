for _ in range(int(input())):
    (n, m) = map(int, input().split())
    A = list(map(int, input().split()))
    ch = 0
    nch = 0
    for i in range(n):
        if A[i] % 2 == 1:
            nch += 1
        else:
            ch += 1
    if n == m:
        if sum(A) % 2 == 1:
            print('Yes')
        else:
            print('No')
    elif ch > 0 and nch > 0:
        print('Yes')
    elif nch > 0 and m % 2 == 1:
        print('Yes')
    else:
        print('No')
