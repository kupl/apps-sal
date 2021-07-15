n = int(input())
a = list(map(int,input().split()))
x = 1
y = 10**9
if n == 1:
    print('YES')
    print(y,x)
else:
    t = 0
    for i in range(1,n):
        s = a[i]-a[i-1]
        if s != 1 and s != -1:
            s = max(s,-s)
            if (x != 1 and x != s) or s == 0:
                print('NO')
                t = 1
                break
            x = s
    if t == 0 and x > 1:
        for i in range(1,n):
            if (a[i] % x == 0 and a[i-1] == a[i]+1) or (a[i-1] % x == 0 and a[i] == a[i-1]+1):
                print('NO')
                t = 1
                break
    if t == 0:
        print('YES')
        print(y,x)
