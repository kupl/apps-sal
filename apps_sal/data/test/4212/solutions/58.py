n,m,q=list(map(int,input().split()))
def dfs(seq):
    u=0
    if len(seq)==n:
        ans=0
        for a,b,c,d in data:
            if seq[b-1]-seq[a-1]==c:
                ans+=d
        return ans
    else:
        for i in range(seq[-1],m+1):
            seq_next=seq+[i]
            u=max(u,dfs(seq_next))
        return u

data=[]
for _ in range(q):
    A=list(map(int,input().split()))
    data.append(A)
print((dfs([1])))

