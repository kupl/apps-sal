n = int(input())
arr = [(abs(i) + abs(j), i, j) for i, j in tuple(list(map(int, input().split())) for i in range(n))]
arr.sort()
ans = []
for z, x, y in arr:
    X, Y = str(abs(x)), str(abs(y))
    l, r, u, d = ' L', ' R', ' U', ' D'
    if x < 0:
        l, r = r, l
    if y < 0:
        u, d = d, u
    if x:
        if y:
            ans += ['1 ' + X + r, '1 ' + Y + u, '2', '1 ' + X + l, '1 ' + Y + d, '3']
        else:
            ans += ['1 ' + X + r, '2', '1 ' + X + l, '3']
    else:
        ans += ['1 ' + Y + u, '2', '1 ' + Y + d, '3']
print(len(ans))
print('\n'.join(ans))
