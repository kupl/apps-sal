n = int(input())
s = [int(i) for i in input().split()]
ans = 0
for i in range(n):
    c = 0
    while s[i] != 0:
        d = s[i]%10
        s[i]//=10
        ans+=d*11*10**c*n
        c+=2
        ans%=998244353
print(ans)
