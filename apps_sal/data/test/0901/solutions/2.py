n, m = map(int, input().split())
flag1 = 0
for i in range(m):
    a = list(map(int, input().split()))
    a = set(a[1:])
    flag = 0
    for x in a:
        if -x in a:
            flag = 1
            break
    if not flag:
        flag1 = 1
        break
print('YES' if flag1 else 'NO')
