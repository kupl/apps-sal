class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxq = collections.deque()
        minq = collections.deque()

        start = 0

        for i, n in enumerate(nums):
            while maxq and maxq[-1][0] < n:
                maxq.pop()
            while minq and minq[-1][0] > n:
                minq.pop()
            maxq.append([n, i])
            minq.append([n, i])

            if maxq[0][0] - minq[0][0] > limit:
                if maxq[0][0] == nums[start]:
                    maxq.popleft()
                if minq[0][0] == nums[start]:
                    minq.popleft()
                start += 1

        return len(nums) - start


#         res = 0
#         maxq = []
#         minq = []
#         j = 0
#         for i,n in enumerate(nums): # O(n)
#             heapq.heappush(maxq, [-n,i] )  # O(log n)
#             heapq.heappush(minq, [n,i] )

#             while -maxq[0][0] - minq[0][0] > limit:
#                 ind = min( maxq[0][1], minq[0][1] )
#                 while maxq[0][1] <= ind:
#                     heapq.heappop(maxq) # O(log n)
#                 while minq[0][1] <= ind:
#                     heapq.heappop(minq)
#                 j = ind+1
#             res = max(res, i - j +1 )

#         return res


#         res = 0

#         i = 0
#         arr = [] # space O(res)
#         for n in nums:  # O(n) time
#             bisect.insort(arr, n) # O(res)
#             while arr[-1] - arr[0] > limit:
#                 ind = bisect.bisect_right(arr, nums[i])  # O( log res )
#                 arr.pop(ind-1)  # O(res)
#                 i += 1
#             res = max(res, len(arr))

#         return res
