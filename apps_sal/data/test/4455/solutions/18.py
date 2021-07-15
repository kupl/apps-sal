from collections import Counter
def search(key,arr):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            break
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return mid

n,q=list(map(int,input().split()))
l=list(map(int,input().split()))
d=dict()
sel=dict(Counter(l))
no=sorted(set(l))
tab=[sel[no[0]]]
for i in range(1,len(no)):
    tab.append(tab[i-1]+sel[no[i]])
for i in range(q):
    li,r=list(map(int,input().split()))
    li-=1
    r-=1
    if li in d:
        d[li].append(r)
    else:
        d[li]=[r]
    
    if r in d:
        d[r].append(li)
    else:
        d[r]=[li]
fin=[]
for i in range(n):
    x=search(l[i],no)
    if x==0:
        sum1=0
    else:
        sum1=tab[x-1]
        if i in d:
            
            for j in range(len(d[i])):
                if l[d[i][j]]<l[i]:
                    sum1-=1
    fin.append(sum1)
print(*fin)

