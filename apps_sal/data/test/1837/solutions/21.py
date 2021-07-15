n=int(input())
a=list(map(int,input().split()))
done=True
ans=0
for i in range(n) :
    if a[i]==i:
        ans+=1
       
    elif done:
        if a[a[i]]==i:
            ans+=2
            done=False

if done and(ans<len(a)-1):ans+=1
print(ans)
    

