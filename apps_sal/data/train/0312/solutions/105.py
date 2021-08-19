class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        nums = [0] + nums

        deque = [(0, 0)]
        cur = 0
        res = 1 + len(nums)

        for i in range(1, len(nums)):
            # print(deque)
            cur += nums[i]
            while deque and cur - deque[0][1] >= k:
                res = min(res, i - deque[0][0])
                deque.pop(0)

            while deque and deque[-1][1] >= cur:
                deque.pop(-1)

            deque.append((i, cur))

        if res > len(nums):
            return -1
        return res
