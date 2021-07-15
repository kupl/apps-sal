# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/721619/Python-Rust-Sliding-Window-and-Deque
'''
The problem description states that we need to find the window with the largest size that has max-min<=limit
This is clearly a sliding window problem. The brute force solution is to start from each index, keep on expanding, and once the max-min is larger than limit, we break. O(n^2)

Can we do better? Well, we can actually use a classic technique in sliding window problems where we keep on expanding the window from the right until the window is no longer valid.
Once the window is invalid we keep on contracting it from the left until it becomes valid again. (Just like in the famous \"Longest Substring Without Repeating Characters\" problem.

Every iteration we need to answer the question, what is our current min and max? this leads us to using two heaps where one of them is a min heap and the other is a max heap.

Every iteration we push the new number to both heaps and then keep on popping from the min and max heaps until we're sure that we've maintained the invariant maxHeap[0] - minHeap[0] <= limit.
We do O(N) pushes and pops from the heaps and each push/pop is O(logN) so we end up with an O(NlogN) solution.

Here is the code:
'''
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minHeap, maxHeap = [], []
        left = maxLen = 0
        
        for right, num in enumerate(nums):
            heappush(minHeap, (num, right))
            heappush(maxHeap, (-num, right))
            
            while num - minHeap[0][0] > limit:
                left = max(left, heappop(minHeap)[1] + 1)
            while -maxHeap[0][0] - num > limit:
                left = max(left, heappop(maxHeap)[1] + 1)
            
            maxLen = max(maxLen, right - left + 1)
        return maxLen
