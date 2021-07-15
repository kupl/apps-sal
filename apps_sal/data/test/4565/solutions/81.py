def schange(s):
    if s=="E":
        return 1
    else:
        return 0

n = int(input())
s = list(map(schange,input()))
ssum = [0]*(n+1)

for i in range(n):
    ssum[i+1] = ssum[i] + s[i]

ans = float('inf')
for i in range(1,n+1):
    turnE = (i-1)-ssum[i-1]
    turnW = ssum[-1] - ssum[i]
    ans=min(ans,turnE+turnW)
    
print(ans)
