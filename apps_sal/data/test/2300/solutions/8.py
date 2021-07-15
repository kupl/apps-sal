n,m = map(int,input().split())
a = list(map(int,input().split()))

f = [1,1]
for i in range(2,n+1):
    f.append(f[i-1] + f[i-2])
    f[i] %= 10 ** 9
    
for q in range(m):
    z,l,r = map(int,input().split())
    if z == 1:
        a[l-1] = r
    else:
        s = 0
        for j in range(l-1,r):
            s += (a[j] * f[j-l+1])
            s %= 10 ** 9 
        print(s)
