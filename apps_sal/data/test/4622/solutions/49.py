n = int(input())
a = list(map(int, input().split()))
a.sort()
before = a[0]
for i in range(1, n):
    if before == a[i]:
        print('NO')
        break
    before = a[i]
else:
    print('YES')
