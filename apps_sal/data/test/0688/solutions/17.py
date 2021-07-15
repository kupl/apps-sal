s=input()
t=input()
a=[0]*10
b=[0]*10 
for i in range(len(s)):
    if s[i]=='5':
        a[2]+=1 
    elif s[i]=='9':
        a[6]+=1 
    else:
        a[int(s[i])]+=1
for i in range(len(t)):
    if t[i]=='5':
        b[2]+=1 
    elif t[i]=='9':
        b[6]+=1 
    else:
        b[int(t[i])]+=1
ans=10**9        
for i in range(10):
    if a[i]!=0:
        ans=min(ans,b[i]//a[i])
print(ans)        

