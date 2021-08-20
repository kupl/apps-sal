n = int(input())
a = [int(x) for x in input().split()]
count = 0
for i in range(2 * n - 1):
    if a[i] < 0:
        count += 1
if n % 2 == 0 and count % 2 != 0:
    for i in range(2 * n - 1):
        if a[i] < 0:
            a[i] = a[i] * -1
    a = sorted(a)
    a[0] = a[0] * -1
    print(sum(a))
else:
    for i in range(2 * n - 1):
        if a[i] < 0:
            a[i] = a[i] * -1
    print(sum(a))
