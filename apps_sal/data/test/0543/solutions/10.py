n = int(input())
a = list(map(int, input().split()))
for (i, j) in enumerate(a):
    if j % 2:
        if i + 1 < n:
            if a[i + 1] == 0:
                print('NO')
                break
            a[i + 1] -= 1
        else:
            print('NO')
            break
else:
    print('YES')
