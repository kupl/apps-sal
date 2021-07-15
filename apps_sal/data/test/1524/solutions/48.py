s=input()
n=len(s)
x=[0]
y=[0]
c=1
for i in range(1,n):
    if s[i-1]=="R" and s[i]=="L":
        x.append(i)
    if s[i-1]=="L" and s[i]=="R":
        y.append(i)
y.append(n)
z=[0]*n
for i in range(1,len(x)):
    z[x[i]-1]+=(x[i]-y[i-1]+1)//2+(y[i]-x[i])//2
    z[x[i]]+=(x[i]-y[i-1])//2+(y[i]-x[i]+1)//2
print(*z)
