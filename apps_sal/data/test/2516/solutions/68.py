n,p = map(int,input().split())
s = input()

ans = 0
ten = 1
d = 0

if (10%p == 0):
    for i in range(n):
        if int(s[i])%p == 0:
            ans += i+1
    print(ans)

else:
    cntlist = [0]*p
    cntlist[0] = 1
    for i in range(n-1,-1,-1):
        a = int(s[i])*ten%p
        d = (d + a)%p
        ten *= 10
        ten %= p
        cntlist[d] += 1

    for i in cntlist:
        ans += i*(i-1)//2
    print(ans)     
