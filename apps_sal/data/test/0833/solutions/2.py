n, v = map(int, input().split())
T = 3010
a = [[] for i in range(T)]
for i in range(n):
    x, y = map(int, input().split())
    a[x].append([y, 1])


ans = 0
for i in range(T):
    a[i] = a[i][::-1]
    j = 0
    cur = v
    while j < len(a[i]):
        if a[i][j][0] > cur:
            ans += cur
            if a[i][j][1] == 0:
                j += 1
            else:
                a[i][j][0] -= cur
            break
        else:
            ans += a[i][j][0]
            cur -= a[i][j][0]
        j += 1
    for t in range(j, len(a[i])):
        if a[i][t][1] != 0:
            a[i + 1].append([a[i][t][0], 0])


print(ans)
