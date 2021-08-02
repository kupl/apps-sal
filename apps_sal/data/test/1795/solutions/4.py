n = int(input())
a = list(map(int, input().split()))
if n == 2:
    print('NO')
else:
    f = 0
    for i in range(n):
        a[i] -= 1
    for i in range(n):
        if a[a[a[i]]] == i:
            f = 1
            break
    if f:
        print('YES')
    else:
        print('NO')
