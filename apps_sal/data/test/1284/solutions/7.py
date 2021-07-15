y=lambda x:print(x)or quit()
n=int(input())
p=list(map(int,input().split()))
if n<2:y(p[0])
if n<4:y(sum(p)-min(p))
s=[p[-1],p[-2]]
r=[p[0],p[1]]
for i in range(2,n):
    r.append(r[-2]+p[i])
    s.append(s[-2]+p[-i-1])
s=s[::-1]
m=r[-1]+r[-2]
for i in range(n-3):m=min(m,r[i]+s[i+3])
m=min([m,r[n-3],s[1],s[2]])
y(r[-1]+r[-2]-m)
