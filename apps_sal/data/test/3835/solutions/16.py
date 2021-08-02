import math
n = int(input(''))
a = []
a.append(0)
for i in range(n):
    ip = list(map(int, input('').split(' ')))
    a.append(ip)
ans = [0] * (n + 1)
ans[3] = math.sqrt((a[3][1] * a[3][0]) // a[2][0])
ans[2] = a[3][1] // ans[3]
ans[1] = a[3][0] // ans[3]
for i in range(3, n + 1, 1):
    ans[i] = a[i][0] // ans[1]
for i in range(1, n + 1, 1):
    print(int(ans[i]), end=' ')
