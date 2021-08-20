(a, b) = map(int, input().split())
flag = True
ans = []
while b > a:
    if b % 2 == 0:
        ans.append(b)
        b //= 2
    elif b % 10 == 1:
        ans.append(b)
        b = (b - 1) // 10
    else:
        b = -1
ans.append(b)
if b != a:
    print('NO')
else:
    print('YES')
    print(len(ans))
    for i in range(len(ans) - 1, -1, -1):
        print(ans[i], end=' ')
