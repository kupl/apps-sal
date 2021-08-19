from heapq import heappush, heappop


class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        maxHeap = []

        def maxHeapPush(val):
            heappush(maxHeap, -val)

        def maxHeapPop():
            return -heappop(maxHeap)

        def maxHeapPeek():
            return -maxHeap[0]

        def maxHeapLen():
            return len(maxHeap)
        for i in range(len(nums)):
            runningSum = 0
            for j in range(i, len(nums)):
                runningSum += nums[j]
                if maxHeapLen() < right:
                    maxHeapPush(runningSum)
                elif maxHeapPeek() > runningSum:
                    maxHeapPop()
                    maxHeapPush(runningSum)
        return sum((maxHeapPop() for _ in range(right - left + 1))) % (10 ** 9 + 7)
