class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        min_lens=[float('inf')]*n
        ans=float('inf')
        cur_sum=0
        min_len=float('inf')
        s=0
        
        for e in range(n):
            cur_sum+=arr[e]
            while cur_sum>target:
                cur_sum-=arr[s]
                s+=1
            if cur_sum==target:
                cur_len=e-s+1
                if s>0 and min_lens[s-1]!=float('inf'):
                    ans=min(ans, cur_len+min_lens[s-1])
                min_len=min(cur_len, min_len)
            min_lens[e]=min_len
            
        return (-1 if ans==float('inf') else ans) 
