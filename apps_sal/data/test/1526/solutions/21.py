a = list(map(int, input().split()))
count = 0
while a[0] != a[1] or a[1] != a[2]:
    a.sort()
    if a[1] != a[2]:
        a[0] += 1
        a[1] += 1
    else:
        a[0] += 2
    count += 1
print(count)

