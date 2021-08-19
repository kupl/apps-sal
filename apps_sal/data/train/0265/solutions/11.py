class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefixsum = {}
        prefixsum[0] = True
        prev = 0
        res = 0
        for num in nums:
            curr = prev + num
            if curr - target in prefixsum:
                res += 1
                prefixsum = {}
                prefixsum[0] = True
                prev = 0
            else:
                prefixsum[curr] = True
                prev = curr
        print(res)
        return res


'\nclass Solution:\n    def maxNonOverlapping(self, nums: List[int], target: int) -> int:\n        \n        prefixsum = {}\n        prefixsum[0] = 0\n        res = 0\n        last = -1\n        prev = 0\n        for idx, num in enumerate(nums):\n            curr = prev + num\n            prefixsum[curr] = idx\n            \n            if curr - target in prefixsum:\n                if prefixsum[curr - target] >= last:\n                    res += 1\n                    last = prefixsum[curr]\n            prev = curr \n        print(prefixsum)\n        print(res)\n        return res\n\n\n'
