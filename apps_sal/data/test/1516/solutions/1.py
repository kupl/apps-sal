n = int(input())

a = list(map(str, input().split()))

ans = 0
for t in a:
    s=''
    for j in t:
        s+=2*j
    ans+=int(s)
    ans%=998244353

print((n*ans)%998244353)

