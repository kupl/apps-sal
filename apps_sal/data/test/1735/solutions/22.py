s=list(input())
d=[s[0]]
count=0
for i in range(1,len(s)):
    if len(d)==0:
        d.append(s[i])
    else:
        x=d.pop()
        if x==s[i]:
            count+=1
        else:
            d.append(x)
            d.append(s[i])
if count%2==0:
    print("No")
else:
    print("Yes")
    
        
    

