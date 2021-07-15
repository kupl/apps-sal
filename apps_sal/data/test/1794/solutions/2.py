n=int(input())
a=list(map(int, input().split()))
a=[ai-1 for ai in a]
a[n:n] = [n - 1]

dp=[0]*n
ans=0
i=n-2

nmax=2**17
tree=[[0,0]]*2*nmax;

#Build Segment tree
j=0
while j<n:
    tree[nmax + j] = [a[j], j]
    j=j+1
j=nmax-1
while j>0:
    tree[j]=max(tree[j*2],tree[j*2+1])
    j=j-1
    
#get max of a interval [left, right]
def get(left, right):
    ans=[-1,-1]
    left=left+nmax
    right=right+nmax+1
    while left<right:
        if (left & 1): 
            ans = max(ans, tree[left])
            left = left + 1
        if (right & 1): 
            right = right - 1
            ans = max(ans, tree[right])
        left = left // 2
        right = right // 2 
    return ans[1]

while i>=0:
    m = get(i + 1, a[i]);
    dp[i] =  dp[m] - (a[i] - m) + n - i - 1
    ans += dp[i]
    i=i-1

print(ans)
