class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) <= 1:
            return len(nums)
        queue = [nums[0]]
        small = queue[0]
        large = queue[0]
        ans = 1
        for i in range(1, len(nums)):
            if abs(nums[i] - small) <= limit and abs(nums[i] - large) <= limit:
                queue.append(nums[i])
                small = min(small, nums[i])
                large = max(large, nums[i])
                ans = max(ans, len(queue))
            else:
                if ans > len(nums) // 2:
                    break
                while queue and (not (abs(nums[i] - small) <= limit and abs(nums[i] - large) <= limit)):
                    queue.pop(0)
                    if queue:
                        small = min(queue)
                        large = max(queue)
                    else:
                        break
                if queue:
                    queue.append(nums[i])
                    small = min(queue)
                    large = max(queue)
                else:
                    queue = [nums[i]]
                    small = nums[i]
                    large = nums[i]
        return ans
