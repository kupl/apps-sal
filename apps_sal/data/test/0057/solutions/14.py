n = int(input())
a = {}
b = {}
for i in range(n):
    t1, t2 = map(int, input().split())
    a[t1] = t1
    b[t2] = t2
if (len(a) < 2 or len(b) < 2):
    print(-1)
else:
    r1 = 0
    flag = 0
    for i in a:
        if (flag == 1):
            r1 -= i
        else:
            r1 += i
            flag = 1
    r2 = 0
    flag = 0
    for i in b:
        if (flag == 1):
            r2 -= i
        else:
            r2 += i
            flag = 1
    r = r1 * r2
    if (r < 0):
        r *= -1
    print(r)
