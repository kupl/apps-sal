n, m = list(map(int,input().split()))
a = list(map(int,input().split()))
z = list(map(int,input().split()))
ch = 0
if  n == sum(z):
    t = 0
    for i in a:
        z[i-1] -= 1
    if z.count(0) == m:
        print('YES')
    else:
        print('NO')

else:
    for i in range(n-sum(z)+1):
        t = 0
        for j in range(1,m+1):
            if a[i:i+sum(z)].count(j) == z[j-1]:
                t+=1
        if t == m:
            print('YES')
            ch = 1
            break
    if ch == 0:
        print('NO')

