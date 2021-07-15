class Solution:
    def findLatestStep(self, arr, k):
        n=len(arr)
        par=[-1]*(n+2)
        count=[0]*(n+1)
        ind=[0]*(n+1)
        ans=-1
        def find(node):
            if par[node]==node:
                return node
            node=par[node]
            return find(node)
        for i in range(n):
            cur=arr[i]
            left=cur-1
            right=cur+1
            par[cur]=cur
            count[cur]+=1
            if par[left]!=-1:
                p=find(left)
                ind[count[p]]-=1
                par[p]=cur
                count[cur]+=count[p]
            if par[right]!=-1:
                p=find(right)
                ind[count[p]]-=1
                par[p]=cur
                count[cur]+=count[p]
            
            ind[count[cur]]+=1
            if ind[k]:
                ans=i+1
        return ans
            

