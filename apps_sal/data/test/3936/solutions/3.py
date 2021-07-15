n = int(input())
s = [input() for _ in range(2)]
mod = 1000000007
cnt = [[0,0,0],[0,2,2],[0,1,3]]
if n==1:
    print(3)
elif n==2:
    print(6)
else:
    c = []
    i = 0
    while i<n:
        if s[0][i]==s[1][i]:
            c.append(1)
            i += 1
        elif i+1<n and s[0][i]==s[0][i+1]:
            c.append(2)
            i += 2
    if c[0]==1:ans = 3
    elif c[0]==2:ans = 6
    for i in range(1,len(c)):
        ans *= cnt[c[i-1]][c[i]]
        ans %= mod

    print(ans%mod)
