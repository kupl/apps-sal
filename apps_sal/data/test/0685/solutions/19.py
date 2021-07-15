n,h = list(map(int,input().split()))
lis=[]
for i in range(n):
    a,b = list(map(int,input().split()))
    lis.append([a,b])
lis.sort()
y=h
cur=ans=i=j=0
lis.append([100000000000,100000000000])
#print(lis)
while i<n and j<n:
    dec = lis[i+1][0]-lis[i][1]
    if dec<y:
        cur+=(lis[i+1][0]-lis[i][0])
        ans = max(ans,cur)
        i+=1
        y-=dec
    else:
        aa=lis[i][1]-lis[i][0]
        ans=max(ans,cur+y+aa)
        y-=dec
        while y<=0 and j<n:
            cur-=(lis[j+1][0]-lis[j][0])
            y+=(lis[j+1][0]-lis[j][1])
#            print(cur,lis[j+1][0]-lis[j][0])
            j+=1    
        cur+=(lis[i+1][0]-lis[i][0])
        i+=1
#        print(cur)
#        ans=max(ans,cur)     
#    print(dec,y,cur,ans)
print(ans)            



