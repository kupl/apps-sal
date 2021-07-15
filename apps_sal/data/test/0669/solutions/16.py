n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
import bisect
a1,a2=[],[]
n1=n//2
app1=a1.append
app2=a2.append
def sums1(i,sum=0):
    if i==n1:
        app1(sum)
    else:
        sums1(i+1,(sum+a[i])%m)
        sums1(i+1,sum)
        
def sums2(i,sum=0):
    if i==n:
        app2(sum)
    else:
        sums2(i+1,(sum+a[i])%m)
        sums2(i+1,sum)

sums1(0)
sums2(n1)

ans=0
end=len(a2)-1

a1=sorted(set(a1))
bis=bisect.bisect_left
for i in a2:
    j=bis(a1,m-i)
    if ans<a1[j-1]+i:
        ans=a1[j-1]+i
print(ans)

