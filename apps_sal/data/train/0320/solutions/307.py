class Solution:

    def minOperations(self, nums: List[int]) -> int:
        count = 0
        res = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                res[i] = nums[i]
        zeros = []
        while res:
            zeros.clear()
            for key in res:
                if res[key] % 2 != 0:
                    res[key] -= 1
                    count += 1
                    minus = True
                if res[key] == 0:
                    zeros.append(key)
            for zero in zeros:
                res.pop(zero)
            if res:
                for key in res:
                    res[key] //= 2
                count += 1
        return count
