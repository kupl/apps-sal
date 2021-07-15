a=input()
b=input()
a1=[0]
curr=0
for i in b:
    if i=='1':
        curr+=1
    a1.append(curr)
a2=[0]
curr=0
for i in b:
    if i=='0':
        curr+=1
    a2.append(curr)
ans=0
for i in range(len(a)):
    if a[i]=='0':
        t=a1[len(b)-len(a)+i+1]-a1[i]
        if t>=0:
            ans+=t
        else:
            break
for i in range(len(a)):
    if a[i]=='1':
        t=a2[len(b)-len(a)+i+1]-a2[i]
        if t>=0:
            ans+=t
        else:
            break
print(ans)

