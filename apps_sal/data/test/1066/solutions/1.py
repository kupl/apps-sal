x= input()
n,k= x.split()
n=int(n)
k=int(k)
if(n%2==0):
    if(k<=n/2):
        ans=2*k-1
    else:
        ans= 2+(k-(int(n/2))-1)*2
else:
    if(k<=(n/2+1)):
        ans=2*k-1
    else:
       ans= 2+(k-(int(n/2)+1)-1)*2
print(int(ans))       

