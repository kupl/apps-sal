class Solution:

    def minOperations(self, nums: List[int]) -> int:
        self.ans = 0
        self.nums = nums

        def manipulate():
            for i in range(len(self.nums)):
                if self.nums[i] % 2 == 1:
                    self.ans += 1
                    self.nums[i] -= 1

            def allEven():
                for num in self.nums:
                    if num % 2 == 1:
                        return False
                return True
            if AllZero():
                return
            while allEven():
                self.nums = [num / 2 for num in self.nums]
                self.ans += 1

        def AllZero():
            for num in self.nums:
                if num != 0:
                    return False
            return True
        while not AllZero():
            manipulate()
        return int(self.ans)
