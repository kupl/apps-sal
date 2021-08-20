n = int(input())
if n % 2:
    a = list(map(int, input().split()))
    s = [[a[0], 0, 0], [0, a[1], 0], [a[0] + a[2], 0, a[2]]] + [[0, 0, 0] for i in range(3, n)]
    for i in range(3, n):
        if i % 2:
            s[i][1] = max(s[i - 2][1], s[i - 3][0]) + a[i]
        else:
            s[i][0] = s[i - 2][0] + a[i]
            s[i][2] = max([s[i - 2][2], s[i - 3][1], s[i - 4][0]]) + a[i]
    print(max([s[-1][2], s[-2][1], s[-3][0]]))
else:
    a = list(map(int, input().split()))
    s = [a[0], a[1]] + [0 for i in range(2, n)]
    for i in range(2, n):
        if i % 2:
            s[i] = max([s[i - 2], s[i - 3]]) + a[i]
        else:
            s[i] = s[i - 2] + a[i]
    print(max(s[-2:]))
