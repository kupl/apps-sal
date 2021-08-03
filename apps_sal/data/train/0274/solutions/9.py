class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # naive method in n2
        # keep track of min and max
        # sliding window: only when exceed limit then contract window

        if not nums:
            return 0

        minDeque = collections.deque()
        maxDeque = collections.deque()
        maxlength = 0
        left = 0
        right = 0

        while right < len(nums):  # not equal sign
            while maxDeque and nums[right] > nums[maxDeque[-1]]:
                maxDeque.pop()
                # decreasign deque
            maxDeque.append(right)

            while minDeque and nums[right] < nums[minDeque[-1]]:
                minDeque.pop()
            minDeque.append(right)

            # it won't be empty, because the \"curr\" element will always be valid
            while abs(nums[maxDeque[0]] - nums[minDeque[0]]) > limit:
                if maxDeque[0] == left:
                    maxDeque.popleft()
                if minDeque[0] == left:
                    minDeque.popleft()
                left += 1

            maxlength = max(maxlength, right - left + 1)
            right += 1

        return maxlength
