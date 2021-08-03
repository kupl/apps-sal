from math import *
n, k = map(int, input().split())
a = []
pre = [0 for i in range(205)]
for i in range(n):
    u, v = map(int, input().split())
    a.append([u, v, i + 1])
    for i in range(u, v + 1):
        pre[i] += 1
ans = []
a.sort()
i = 1
while(1):
    flag = 0
    for i in range(205):
        if pre[i] > k:
            flag = i
            break
    if flag == 0:
        break
    m = 0
    m1 = 0
    for i in range(n):
        if a[i][0] > flag:
            break
        if m < a[i][1]:
            m = a[i][1]
            m1 = i
    ans.append(a[m1][2])
    for i in range(a[m1][0], a[m1][1] + 1):
        pre[i] -= 1
    del(a[m1])
    n -= 1
print(len(ans))
for i in ans:
    print(i, end=" ")
print()
