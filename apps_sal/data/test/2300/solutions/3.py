n,m = list(map(int,input().split()))
d = [int(x) for x in input().split()]
f = [1,1]
for i in range(n):
    f.append((f[-1]+f[-2])% 1000000000)
for i in range(m):
    s = [int(x) for x in input().split()]
    if s[0] == 1:
        x = s[1]-1
        v = s[2]
        d[x] = v
    elif s[0] == 2:
        r = s[2]-1
        l = s[1]-1
        ans = 0
        for i in range(r-l+1):
            #print("(",f[i],d[i+l],ans,")")
            ans = (ans % 10**9 + d[i+l]% 10**9 * f[i] % 10**9)% 10**9
        print(ans) 
    elif s[0] == 3:
        r = s[2]-1
        l = s[1]-1  
        x = s[3]
        for i in range(l,r+1):
            d[i] += x

