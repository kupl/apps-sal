class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        '''
        The idea is to keep track of range sums starting from nums[i] (i=0...n-1) in parallel in a priority queue of size n. In the beginning, the queue is initialized with (nums[i], i), i.e. just the starting element and its position. At each following step, pop the smallest x, i out of the queue, and perform below operations:

check if step has reached left, add x to ans;
extend the range sum x (currently ending at i) by adding nums[i+1] and in the meantime update the ending index to i+1.
After right steps, ans would be the correct answer to return.

O(N^2 logN) worst (but much faster on average) & O(N) space (32ms 100%)
        '''
        h = [(x, i) for i, x in enumerate(nums)]  # min-heap
        heapify(h)

        ans = 0
        for k in range(1, right + 1):  # 1-indexed
            x, i = heappop(h)
            if k >= left:
                ans += x
            if i + 1 < len(nums):
                heappush(h, (x + nums[i + 1], i + 1))

        return ans % 1_000_000_007
