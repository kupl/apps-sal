import string
import math

line=input()
n=int(line.split(" ")[0])
k=int(line.split(" ")[1])

def search(l,r,k,dep):
    mid=(l+r)/2
    if k==mid or l==r:
        return(dep)
    if k<mid:
        return search(l,mid-1,k,dep-1)
    if k>mid:
        return search(mid+1,r,k,dep-1)

print(search(1,pow(2,n)-1,k,n))

