(n, s) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if a[0] == 0:
    print('NO')
elif a[s - 1] == 1:
    print('YES')
elif b[s - 1] == 0:
    print('NO')
else:
    for i in range(s, n):
        if a[i] == 1 and b[i] == 1:
            print('YES')
            break
    else:
        print('NO')
