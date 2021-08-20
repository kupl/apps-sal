n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1):
    if a[i] > 0:
        a[i] %= 2
    if a[i] == 1:
        a[i + 1] -= 1
if a[-1] % 2 != 0:
    a[-1] = -1
if min(a) >= 0:
    print('YES')
else:
    print('NO')
