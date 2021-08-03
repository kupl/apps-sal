class Solution:
    # def longestSubarray(self, nums: List[int], limit: int) -> int:
    #     start=0
    #     end=1
    #     result=1
    #     while end<len(nums):
    #         tmp=nums[end]
    #         flag=0
    #         for i in range(start,end):
    #             if abs(nums[i]-tmp)>limit:
    #                 flag=1
    #                 start=i
    #         if flag==0:
    #             if end-start+1>result:
    #                 result=end-start+1
    #             end+=1
    #         else:
    #             start+=1
    #     return result
    def longestSubarray(self, A, limit):
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(A):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i:
                    heapq.heappop(maxq)
                while minq[0][1] < i:
                    heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res
