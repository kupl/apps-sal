def dfs(left,right):
    if right-left==1:
        return h[left]
    elif right-left<=0:
        return 0
    else:
        ret=min(h[left:right])
        k=0
        for i in range(left,right):
            h[i]-=ret
            if h[i]==0:
                k=i
        ret+=dfs(left,k)
        ret+=dfs(k+1,right)
        return ret

N=int(input())
h=list(map(int,input().split()))

print((dfs(0,N)))

