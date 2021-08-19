(a, b) = [int(x) for x in input().split()]
ans = [b]
while b > a:
    if b % 2 == 1 and str(b)[-1] != '1':
        print('NO')
        break
    if b % 2 == 1 and str(b)[-1] == '1':
        b = b // 10
        ans.append(b)
        continue
    if b % 2 == 0:
        b = b // 2
        ans.append(b)
        continue
else:
    if b != a:
        print('NO')
    else:
        print('YES')
        print(len(ans))
        for i in range(len(ans)):
            print(ans[len(ans) - i - 1], end=' ')
