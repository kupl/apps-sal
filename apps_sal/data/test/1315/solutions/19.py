n = int(input().strip())
a = list(map(int, input().strip().split()))
for i in range(n):
    a[i] = a[i] - (n - i)
a.sort()
for i in range(n):
    a[i] = a[i] + (n - i)
ans = True
for i in range(n - 1):
    if a[i] > a[i + 1]:
        ans = False
        break
if ans:
    for i in range(n):
        tmp = ' ' if i != n - 1 else '\n'
        print(a[i], end=tmp)
else:
    print(':(')
