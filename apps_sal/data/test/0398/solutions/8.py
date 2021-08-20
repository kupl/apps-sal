n = int(input())
a = list(map(int, input().split()))
a.sort()
f = False
for i in range(n - 2):
    if a[i] + a[i + 1] > a[i + 2]:
        f = True
if f:
    print('YES')
else:
    print('NO')
