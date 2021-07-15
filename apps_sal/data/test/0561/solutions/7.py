import sys 
n = int(input())
a = sorted(list(map(int,input().split())))
if n == 1:
    print(-1)
else:
    d = a[1] - a[0]
    x = 0
    v = 0
    t = -1
    v1 = 0
    t1 = -1
    for i in range(1, n):
        if (a[i] - a[i-1] == d):
            x += 1
        elif (a[i] - a[i-1] == 2 * d):
            v += 1
            t = i-1
        elif (2 * (a[i] - a[i-1]) == d):
            v1 += 1
            t1 = i-1
        else:
            print(0)
            return
        if v >= 2:
            print(0)
            return
    if v == 1:
        print(1)
        print(a[t] + d)
        return
    if (v1 > 0) and (v1 + 1 < n - 1):
        print(0)
        return
    if (v1 > 0) and (v1 + 1 == n - 1):
        print(1)
        print(a[0] + d // 2)
        return
    if d == 0:
        print(1)
        print(a[0])
        return
    ans = [a[0] - d]
    if n == 2:
        if d % 2 == 0:
            ans.append(a[0] + (d // 2))
    ans.append(a[n - 1] + d)
    print(len(ans))
    for i in ans:
        print(i, end = ' ')
