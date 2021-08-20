q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(0, 2 * n, 2):
        if a[i] != a[i + 1] or a[-i - 1] != a[-i - 2]:
            print('NO')
            break
        if i == 0:
            area = a[i] * a[-i - 1]
        elif area != a[i] * a[-i - 1]:
            print('NO')
            break
    else:
        print('YES')
