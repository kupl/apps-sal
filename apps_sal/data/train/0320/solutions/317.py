class Solution:
    def minOperations(self, nums: List[int]) -> int:
        zeros = sum([num == 0 for num in nums])
        odds = set([i for i in range(len(nums)) if nums[i] % 2])
        n = len(nums)
        count = 0
        while zeros < n:
            if odds:
                for oddidx in odds:
                    nums[oddidx] = nums[oddidx] - 1
                    if nums[oddidx] == 0:
                        zeros += 1
                count += len(odds)
                odds = set()
            else:
                for i in range(n):
                    if nums[i] > 0:
                        nums[i] = nums[i] // 2
                        if nums[i] % 2:
                            odds.add(i)
                count += 1
        return count
