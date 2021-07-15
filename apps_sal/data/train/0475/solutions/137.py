class Solution:
    def rangeSum1(self, nums: List[int], n: int, left: int, right: int) -> int:
        '''
        TC: n^2log(n)
        SC: n^2
        '''
        subarraySum = []
        for i in range(n):
            s = 0
            for j in range(i,n):
                s += nums[j]
                subarraySum.append(s)
        subarraySum.sort()
        ans = sum(subarraySum[left-1:right])
        return ans%(10**9+7)
                
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        h = [(v,i) for i,v in enumerate(nums)]
        heapify(h)
        
        ans = 0
        for k in range(1,right+1):
            v,i = heappop(h)
            if k >= left:
                ans += v
            if i+1 < n:
                heappush(h,(v+nums[i+1],i+1))
        return ans%(10**9+7)
