class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n=len(arr)
        if n==1 or d==0:
            return 1
        e=[[]for i in range(n)]
        for i in range(0,n):
            for j in range(i-1,max(0,i-d)-1,-1):
                if arr[j]<arr[i]:
                    e[i].append(j)
                else :
                    break;
            for j in range(i+1,min(n-1,i+d)+1):
                if arr[j]<arr[i]:
                    e[i].append(j)
                else :
                    break;
        ans=1
        queue=[]
        cnt=[1for i in range(n)]
        for i in range(0,n):
            queue.append([arr[i],i])
        queue.sort()
        for i in range(0,n):
            u=queue[i][1]
            for v in e[u]:
                cnt[u]=max(cnt[u],cnt[v]+1)
            ans=max(ans,cnt[u])
        return ans

