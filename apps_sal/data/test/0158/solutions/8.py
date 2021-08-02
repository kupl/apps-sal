n = int(input())
a = list(map(int, input().strip().split(' ')))
a.sort()
if a[n - 1] < a[n]:
    print('YES')
else:
    print('NO')
