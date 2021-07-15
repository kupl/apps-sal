n,m = map(int,input().split())
ans = []
for i in range(m):
    a,b = map(int,input().split())
    ans.append(a)
    ans.append(b)

for j in range(1,n+1):
    print(ans.count(j))
