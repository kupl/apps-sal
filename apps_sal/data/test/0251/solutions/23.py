
n,k=list(map(int,input().split()))

h=list(map(int,input().split()))
min1=min(h)

m=max(h)+1 - min1
a=[0 for i in range(m+5)]

for i in range(n):
    h[i]-=min1
    a[h[i]]+=1

for i in range(m-2,-1,-1):
    a[i]+=a[i+1]
cnt=0
cnt1=0
#print(a)
for i in range(m-1,0,-1):
    if(cnt1+a[i]>k):
        cnt1=a[i]
        cnt+=1
    else:
        cnt1+=a[i]
if(cnt1):
    cnt+=1
print(cnt)
    
    
    


    



