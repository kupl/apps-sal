n = int(input())
a = list(map(int, input().split()))
i = 0
while i + 1 < n and a[i] < a[i + 1]:
    i += 1
if i + 1 == n:
    print('YES')
else:
    while i + 1 < n and a[i] == a[i + 1]:
        i += 1
    if i + 1 == n:
        print('YES')
    else:
        while i + 1 < n and a[i] > a[i + 1]:
            i += 1
        if i + 1 == n:
            print('YES')
        else:
            print('NO')
