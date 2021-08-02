n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s -= 1
if a[0] == 0:
    print('NO')
elif a[s] == 0 and b[s] == 0:
    print('NO')
elif a[s] == 0:
    ok = False
    for i in range(s + 1, n):
        if a[i] == 1 and b[i] == 1:
            print('YES')
            ok = True
            break
    if not ok:
        print('NO')
else:
    print('YES')
