n = int(input())
a = [int(i) for i in input().split()]
for i in range(n):
    if a[i] < 0:
        print('NO')
        raise SystemExit
    if a[i] % 2 != 0:
        if i == n - 1:
            print('NO')
            raise SystemExit
        else:
            a[i + 1] -= 1
print('YES')
