class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decStack = collections.deque()
        incStack = collections.deque()
        ans = 0
        l = 0
        for (r, n) in enumerate(nums):
            while decStack and decStack[-1][0] <= n:
                decStack.pop()
            decStack.append((n, r))
            while incStack and incStack[-1][0] >= n:
                incStack.pop()
            incStack.append((n, r))
            while decStack[0][0] - incStack[0][0] > limit:
                l = min(incStack[0][1], decStack[0][1]) + 1
                while decStack and decStack[0][1] < l:
                    decStack.popleft()
                while incStack and incStack[0][1] < l:
                    incStack.popleft()
            ans = max(ans, r - l + 1)
        return ans
