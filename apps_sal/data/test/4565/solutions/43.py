n=int(input())
s=input()
v=[0 for i in range(n)]

for i in range(n):
    j=0
    if s[i]=="E":
        j=1
    else:
        j=-1
    if i==0:
        v[i]+=j
    else:
        v[i]+=j+v[i-1]

sum=-2
w=0
res=""
for i in range(n):
    if sum<v[i]:
        sum=v[i]
        wmax=w
        emax=i-w
        res=s[i]
    if s[i]=="W":
        w+=1

if res=="W":
    print((wmax+s.count("E")-emax))
else:
    print((wmax+s.count("E")-emax-1))

