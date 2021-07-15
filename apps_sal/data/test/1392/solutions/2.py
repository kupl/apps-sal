n,m=map(int,input().split())
ans = 0
for i in range(n):
    a = input().strip()
    c = [True]*(m+1)
    for k in a:
        if k<=str(m):
            c[int(k)] = False
    if c.count(True)==0:
        ans+=1
print(ans)
