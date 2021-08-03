t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    p = b[0]
    f = False
    for j in range(n):
        if a[j] % p != 0:
            if a[j] != b[j]:
                f = True
    if f:
        print('NO')
    else:
        print('YES')
