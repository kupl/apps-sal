n = int(input())
a = list(map(int, input().split()))
f = 0
for i in range(1, n):
    if f == 0 and a[i] == a[i - 1]:
        f = 1
    elif f == 0 and a[i] < a[i - 1]:
        f = 2
    elif f == 1 and a[i] < a[i - 1]:
        f = 2
    elif f == 0 and a[i] > a[i - 1] or (f == 1 and a[i] == a[i - 1]) or (f == 2 and a[i] < a[i - 1]):
        continue
    else:
        f = -1
        break
if f == -1:
    print('NO')
else:
    print('YES')
