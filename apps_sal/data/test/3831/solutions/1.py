n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    a[i][1] += a[i][0]
for i in range(1, n):
    if a[i][1] > a[i - 1][1] + 1:
        a[i][1] = a[i - 1][1] + 1
        if a[i][1] < a[i][0]:
            print(-1)
            return()
s = a[-1][1] - a[-1][0]
for i in range(n - 2, -1, -1):
    if a[i][1] > a[i + 1][1] + 1:
        a[i][1] = a[i + 1][1] + 1
        if a[i][1] < a[i][0]:
            print(-1)
            return()
    s += a[i][1] - a[i][0]
print(s)
for i in a:
    print(i[1], end=' ')
