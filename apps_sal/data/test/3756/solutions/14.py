n,t=list(map(int,input().split()))
s=input()
ans=[]
te=[]
for i in range(len(s)):
    if(s[i]=='.'):
        for j in range(i+1,len(s)):
            ans.append(int(s[j]))
        break;
    te.append(int(s[i]))
    
flag=0
for i in range(len(ans)):
    if(ans[i]>=5):
        flag=1
        break;
if(flag==0):
    print(s)
    return
ans=ans[0:i+1]
pre=[0 for i in range(len(ans))]
for i in range(1,len(ans)):
    if(ans[i-1]>=5):
        pre[i]=pre[i-1]+1
    else:
        pre[i]=pre[i-1]
    
shrink=[0 for i in range(len(ans))]
car=0
for i in range(len(ans)-1,-1,-1):
    if(i==len(ans)-1):
        car=1
        shrink[i]=1
        t-=1
    else:
        if(car==1):
            ans[i]+=1
            
        if(ans[i]<5):
            car=0
            continue;
        elif(5<=ans[i]<=9):
            car=0
            if(pre[i]>0):
                continue;
            else:
                if(t==0):
                    car=0
                    break;
                else:
                    t-=1
                    shrink[i]=1
                    car=1
        else:
            shrink[i]=1
            car=1
    
if(car==1):
    for i in range(len(te)-1,-1,-1):
        if(te[i]==9 and i>0):
            te[i]=0
        elif(te[i]<9):
            te[i]+=1
            car=0
            break;
if(car==1):
    te=[1]+[0]*len(te)

x=shrink.index(1)
if(x==0):
    print(''.join(map(str,te)))
    return
else:
    ans=ans[0:x]
    print(''.join(map(str,te))+'.'+''.join(map(str,ans)))
    
        
            
            
        
        

