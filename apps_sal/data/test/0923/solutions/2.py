n = int(input())
a = list(map(int, input().split()))
if a[0] == 0:
    r = 0
else:
    r = n - a[0]
f = True
for i in range(n):
    if i % 2 == 0:
        a[i] += r
    else:
        a[i] -= r
    a[i] = a[i] % n
    if i > 0 and a[i] != a[i - 1] + 1:
        f = False
        print('No')
        break
if f:
    print('Yes')
