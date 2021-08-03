class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def cod(k, i):
            if k == 0:
                self.memo[k] = [self.g[i], self.h[i]]
                return 0
            if k not in self.memo:
                if k % 2 == 0:
                    self.g[i] += 1
                    cod(int(k / 2), i)
                else:
                    self.h[i] += 1
                    cod(k - 1, i)

        self.memo = {}
        l = len(nums)
        f = [0] * l
        self.g = [0] * l
        self.h = [0] * l
        for i in range(l):
            f[i] = cod(nums[i], i)
        return sum(self.h) + max(self.g)
