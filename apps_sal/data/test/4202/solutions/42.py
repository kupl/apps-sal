import sys
L,R = map(int,input().split())
mod = 2019
if R - L >= 2019:
    print(0)
else:
    ans = 10**8
    for i in range(L,R):
        for j in range(i+1,R+1):
            if i * j % mod == 0:
                print(0)
                return
            ans = min(ans,(i*j)%mod)
    print(ans)
