n, k = list(map(int, input().split()))
data = input()
a = {}
for i in data:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
for i in list(a.values()):
    if i > k:
        print('NO')
        break
else:
    print('YES')
