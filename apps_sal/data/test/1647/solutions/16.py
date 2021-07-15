def find(x,parent,rank):
    if(parent[x]!=x):
        parent[x]=find(parent[x],parent,rank)
    return parent[x]

def union(x,y,parent,rank):
    
    xroot=parent[x]
    yroot=parent[y]
    
    if(rank[xroot]<rank[yroot]):
        parent[xroot]=yroot
    elif(rank[xroot]>rank[yroot]):
        parent[yroot]=xroot
    else:
        parent[yroot]=xroot
        rank[xroot]+=1
    
    
    
n=int(input())
str1=input()
str2=input()

hashd=dict()
rev=dict()
i=0
k=0
while(i<len(str1)):
    if(str1[i] not in hashd):
        hashd[str1[i]]=k
        rev[k]=str1[i]
        k+=1
    i+=1
i=0
while(i<len(str2)):
    if(str2[i] not in hashd):
        hashd[str2[i]]=k
        rev[k]=str2[i]
        k+=1
    i+=1

rank=[0 for x in range(k)]
parent=[x for x in range(k)]
sums=0
i=0
arr1=[]
arr2=[]
while(i<n):
    if(find(hashd[str1[i]],parent,rank)!=find(hashd[str2[i]],parent,rank)):
        sums+=1
        union(hashd[str1[i]],hashd[str2[i]],parent,rank)
        arr1.append(str1[i])
        arr2.append(str2[i])
    i+=1
print(sums)
i=0
while(i<len(arr1)):
    print(arr1[i]+' '+arr2[i])
    i+=1

