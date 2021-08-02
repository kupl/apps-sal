
n = int(input())
a = list(map(int, input().split()))
ok = True

for i in range(n - 1):
    if abs(a[i] - a[i + 1]) > 1:
        ok = False

if ok:
    print('YES')
else:
    print('NO')
