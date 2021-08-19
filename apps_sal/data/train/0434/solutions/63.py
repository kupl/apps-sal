class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        earliest_one = float('inf')
        earliest_zero = float('inf')
        zeros = 1
        max_len = 0
        while r < len(nums):
            zeros -= nums[r] == 0
            if zeros < 0:
                zeros += nums[l] == 0
                l += 1
            r += 1
        return r - l - 1
        '#queue kind of slow\n        l = 0\n        r = 0\n        max_len = 0\n        zeros = 0\n        queue = []\n        while(r < len(nums)):\n            if(nums[r] == 0 and zeros < 1):\n                zeros = 1\n                queue.append(nums[r])\n                max_len = max(max_len, len(queue))\n                r += 1\n            elif(nums[r] == 0 and zeros == 1):\n                if(queue[0] == 0):\n                    #zero in front\n                    while(len(queue) > 0 and queue[0] == 0):\n                        queue.pop(0)\n                #zero in the middle\n                else:\n                    while(len(queue) > 0 and queue[0] == 1):\n                        queue.pop(0)\n                    queue.pop(0)\n                queue.append(nums[r])\n                max_len = max(max_len, len(queue))\n                r += 1\n            elif(nums[r] == 1):\n                queue.append(nums[r])\n                max_len = max(max_len, len(queue))\n                r += 1\n        return max_len-1'
