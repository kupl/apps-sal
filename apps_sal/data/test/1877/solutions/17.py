n=int(input())
x=0
y=0
s=input()
l=[]
for i in range(0,len(s)):
    if s[i]=='R':
        x+=1
    else:
        y+=1
    l.append(x-y)
if n<=2:
    print(0)
else:
    c=0
    for j in range(1,n-1):
        if l[j]==0 and l[j-1]*l[j+1]<0:
            c+=1
    print(c)


