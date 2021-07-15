a=input()
b=input()
dict1={}
dict2={}
for i in range (0,len(a)):
    if a[i] in dict1:
        dict1[a[i]]+=1
    else:
        dict1[a[i]]=1

act=set()
for j in range (0,len(b)):
    act.add(b[j])
    if b[j] in dict2:
        dict2[b[j]]+=1
    else:
        dict2[b[j]]=1
        if (b[j] not in dict1):
            dict1[b[j]]=0


z=list(act)
ctr=0
char=0
for i in range (0,len(z)):
    ctr+=min(dict1[z[i]],dict2[z[i]])
    if (min(dict1[z[i]],dict2[z[i]])!=0):
        char+=1

if (ctr>0 and char==len(z)):
    print (ctr)
else:
    print(-1)
    
        
        
    
    

