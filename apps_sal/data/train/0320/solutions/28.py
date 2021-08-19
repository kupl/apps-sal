class Solution:
    def minOperations(self, nums: List[int]) -> int:

        def operate(n):
            max_ = 0
            ans = 0
            k = 0
            while n > 0:
                k += 1
                ans += n % 2
                n = n // 2
            max_ = max(max_, k - 1)
            return max_, ans

        ans = 0
        max_ = 0
        for n in nums:
            m, o = operate(n)
            # print(m,n,o)
            max_ = max(max_, m)
            ans += o

        return ans + max_
