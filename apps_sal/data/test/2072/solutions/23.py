n=int(input())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))

def fin(a) :
    k=0
    for i in range(n) :
        k=max(abs(l[i]-a)/l1[i],k)
    return k
left=1
right=1e9

while (abs(left-right)>5e-7) :
    
    mid=(left+right)/2
    if (fin(mid-4e-6)<fin(mid+4e-6)):
	    right=mid
    else:
	    left=mid
    
    
print(fin(left))

