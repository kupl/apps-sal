n = int(input())
a = list(map(int, input().split()))
fl = False
ans = True
for i in range(n - 1):
    if a[i + 1] > a[i]:
        if fl:
            ans = False
    else:
        fl = True
if ans:
    print('YES')
else:
    print('NO')
