def R():
    return list(map(int, input().split()))


n = R()[0]
a = R()
for i in range(n):
    a[i] += i
a = sorted(list(set(a)))
if len(a) != n:
    print(':(')
else:
    for i in range(n):
        print(a[i] - i, end=' ')
