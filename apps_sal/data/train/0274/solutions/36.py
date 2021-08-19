from heapq import heapify, heappop, heappush


class Solution:
    def longestSubarray(self, lis: List[int], limit: int) -> int:
        n = len(lis)
        miheap = []
        mxheap = []
        heapify(miheap)
        heapify(mxheap)
        ans = 1
        heappush(miheap, [lis[0], 0])
        heappush(mxheap, [-lis[0], 0])
        tmp = 0
        for i in range(1, n):
            heappush(miheap, [lis[i], i])
            heappush(mxheap, [-lis[i], i])
            while miheap and abs(miheap[0][0] + mxheap[0][0]) > limit:
                tmp = min(mxheap[0][1], miheap[0][1]) + 1
                while mxheap[0][1] < tmp:
                    heapq.heappop(mxheap)
                while miheap[0][1] < tmp:
                    heapq.heappop(miheap)
            ans = max(ans, i - tmp + 1)
            # print(miheap,mxheap)
        return ans
