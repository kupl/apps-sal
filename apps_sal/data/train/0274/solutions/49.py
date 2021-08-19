import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        # sliding window, but we only need to keep the min and max in this window along with the index. at the same time, we set a variable, to check what is the window starting point, we will do
        length = len(nums)
        start = 0
        min_heap = []
        max_heap = []

        res = 1
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, -i))
            heapq.heappush(max_heap, (-num, -i))
            # while -min_heap[0][1] < start:
            #     heapq.heappop(min_heap)
            # while -max_heap[0][1] < start:
            #     heapq.heappop(max_heap)

            # bug bug here: 加入出现现在的number导致超过了limit，那么你需要一直移动自动你找到一个index；
            while -max_heap[0][0] - min_heap[0][0] > limit:
                start += 1
                while -min_heap[0][1] < start:
                    heapq.heappop(min_heap)
                while -max_heap[0][1] < start:
                    heapq.heappop(max_heap)

            res = max(res, i - start + 1)

        return res
