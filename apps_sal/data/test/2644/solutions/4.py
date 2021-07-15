n = int(input())
p = list(map(lambda x:int(x)-1,input().split()))

q = [0]*n
for i in range(n):
    q[p[i]] = i

ans = []
i = 0
while i<n:
    idx = q[i]
    if i<idx:
        for j in range(idx-1,i-1,-1):
            p[j],p[j+1] = p[j+1],p[j]
            ans.append(str(j+1))
        i = idx
    else:
        i += 1
if len(ans)==n-1 and all([p[i]==i for i in range(n)]):
    print("\n".join(ans))
else:
    print(-1)
