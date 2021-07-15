n,m=list(map(int,input().split()))
a = list(map(int,input().split()))
t = list(map(int,input().split()))
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
g = a[1]-a[0]
for i in range(n-1):
    g = gcd(g,a[i+1]-a[i])
    if g==1:
        break
idx=-1
for i in range(m):
    if g%t[i]==0:
        idx=i
        break
    
if idx==-1:
    print("NO")
else:
    print("YES")
    print(a[0],idx+1)

