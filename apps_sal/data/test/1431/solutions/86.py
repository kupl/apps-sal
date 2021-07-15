icase=0
if icase==0:
    n=int(input())
    a=[0]+list(map(int,input().split()))
elif icase==3:
    f=open(r"C:\Users\nishi\999atcoder\ABCD040-151\ABC134D\testcase_12.in")
    ll=f.readline()
    n=int(ll)
    ll=f.readline()
    a=[0]+list(map(int,ll.split()))
    f.close()
b=[0]*(n+1)
for i in range(n//2+1,n+1):
    b[i]=a[i]
#    print(i,a[i])
    
for i in range(n//2,0,-1):
    i2=i*2
    asum=0
    while i2<=n:
        asum+=b[i2]
        i2+=i
    b[i]=(asum+a[i])%2
#    print(i,b[i],a[i],asum)
    
print(sum(b))
for i in range(1,len(b)):
    if b[i]==1:
        print(i,end=" ")
print(" ")
