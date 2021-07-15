n=int(input())
def getsum(BITTree,i): 
    s = 0 #initialize result 
  
    # index in BITree[] is 1 more than the index in arr[] 
    i = i+1
  
    # Traverse ancestors of BITree[index] 
    while i > 0: 
  
        # Add current element of BITree to sum 
        s += BITTree[i] 
  
        # Move index to parent node in getSum View 
        i -= i & (-i) 
    return s 
  
# Updates a node in Binary Index Tree (BITree) at given index 
# in BITree. The given value 'val' is added to BITree[i] and 
# all of its ancestors in tree. 
def updatebit(BITTree , n , i ,v): 
  
    # index in BITree[] is 1 more than the index in arr[] 
    i += 1
  
    # Traverse all ancestors and add 'val' 
    while i <= n: 
  
        # Add 'val' to current node of BI Tree 
        BITTree[i] += v 
  
        # Update index to that of parent in update View 
        i += i & (-i) 
a=list(map(int,input().split()))
# print(*a)
pre=dict()
pos=dict()
for i in range(n):
    if(pre.get(a[i],None)==None):
        pre[a[i]]=0
    # if(pos.get(a[n-1-i],None)==None):
    #     pos[a[n-1-i]]=0 
    pre[a[i]]+=1 
    # pos[a[n-1-i]]+=1 
ans=0
BIT=[0]*(n+1)
for i in range(n-1,0,-1):
    # print(i)
    pre[a[i]]-=1 
    if(pos.get(a[i],None)==None):
        pos[a[i]]=0
    pos[a[i]]+=1 
    # print(pre)
    # print(pos)
    updatebit(BIT,n,pos[a[i]],1)
    # for j in range(7):
    #     print(getsum(BIT,j),end=' ')
    # print()
    #     print(getsum(BIT,j),end=' ')
    # print()
    # if pos[a[i]]>1:
    #     updatebit(BIT,n,pos[a[i]]-1,-1)
    # for j in range(7):
    temp=getsum(BIT,pre[a[i-1]]-1)
    ans+=temp
    # print(temp,pre[a[i-1]]-1,a[i-1],i)
print(ans)

