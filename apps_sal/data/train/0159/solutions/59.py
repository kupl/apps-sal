class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=[0]*n
        remove=collections.defaultdict(int)
        h=[]
        def get_b():
            if not h:
                return 0
            b=heapq.heappop(h)
            while remove[b]>0:
                remove[b]-=1
                b=heapq.heappop(h)
            heapq.heappush(h,b)
            return -b
        for i,d in enumerate(nums):
            if i>k:
                remove[-dp[i-k-1]]+=1
            dp[i]=max(get_b(),0)+d
            heapq.heappush(h,-dp[i])
        return max(dp)
