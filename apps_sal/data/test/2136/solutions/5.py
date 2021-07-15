def st(a, b):
    return str(a + 1) + ' ' + str(b + 1)


ans = []
for _ in range(int(input())):
    n = int(input())
    u = []
    for i in range(n):
        u.append(list(input()))
    a = [u[0][1], u[1][0], u[n - 1][n - 2], u[n - 2][n - 1]]
    if a[0] == a[1] and a[2] == a[3]:
        if a[1] != a[2]:
            ans.append(0)
        else:
            ans.append(2)
            ans.append(st(0, 1))
            ans.append(st(1, 0))
    elif a[0] == a[1]:
        ans.append(1)
        if a[2] == a[1]:
            ans.append(st(n - 1, n - 2))
        else:
            ans.append(st(n - 2, n - 1))
    elif a[2] == a[3]:
        ans.append(1)
        if a[0] == a[2]:
            ans.append(st(0, 1))
        else:
            ans.append(st(1, 0))
    else:
        ans.append(2)
        if a[0] == a[2]:
            ans.append(st(0, 1))
            ans.append(st(n - 2, n - 1))
        else:
            ans.append(st(0, 1))
            ans.append(st(n - 1, n - 2))
print('\n'.join(map(str, ans)))

