n,a = list(map(int,input().split()))
d = list(map(int,input().split()))
s = sum(d)
ans = []
for i in range(n):
        l = max(1,a-(s-d[i]))
        r = min(d[i],a-(n-1))
        ans.append(d[i]-(r-l+1))
print(' '.join(map(str,ans)))

