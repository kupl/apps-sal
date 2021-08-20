n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        if a[j] > a[i]:
            t = a[j]
            a[j] = a[i]
            a[i] = t
            count += 1
if count > 1:
    print('NO')
else:
    print('YES')
