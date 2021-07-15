def fact(n):
    if(n==0):
        return 1;
    return(n*fact(n-1))
mod=1000000007
ncrtable=[[0 for i in range(1001)] for j in range(1001)];
ncrtable[0][0]=1;
for row in range(1,1001):
    for col in range(row+1):
        if(col==0):
            ncrtable[row][col]=1;
        else:
            ncrtable[row][col]=ncrtable[row-1][col]+ncrtable[row-1][col-1];
        
def ncr(n,r):
    if(n<r):
        return 0;
    if(r<0):
        return 0;
    return ncrtable[n][r];
def compute(n,x):
    tot=0;
    #cnt=0;
    y=x;
    for i in range(1000,-1,-1):
        if(1<<i & n):
            tot+=ncr(i,x)%mod;
            tot%=mod
            x-=1;
            #cnt+=1;
    if(x==0):
        return((tot+1)%mod);
    return(tot%mod);
arr=[0 for i in range(1002)];
arr[1]=1;
for i in range(2,1001):
    ct=0
    for j in range(32,-1,-1):
        if(1<<j & i):
            ct+=1;
    arr[i]=arr[ct]+1
n=int(input(),2);
#print(n);
   
k=int(input())
ans=0
for i in range(0,1001):
    if(arr[i]==k):
        ans=compute(n,i)+ans;
        ans%=mod;
if(k==1):
    ans-=1;

print(ans);
return
if(n>=1001):
    for i in range(0,1001):
        if(arr[i]==k-1):
            ans=compute(n,i)+ans;
            #ans-=1;
            ans%=mod;
#for i in range(1,1001):
 ##  for j in range(32):
   #     if(1<<j &i):
    #        c+=1;
   # if(c==k-1):
    #    ans+=(mod-1);
     #   ans%=mod;
    
if(k!=1):        
    print(ans);
else:
    print((ans-1));

