class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        num_zero = sum(n == 0 for n in nums)
        while num_zero != len(nums):
            for i, n in enumerate(nums):
                if n % 2 == 1:
                    ans += 1
                    nums[i] -= 1
                    if nums[i] == 0:
                        num_zero += 1
                nums[i] >>= 1
            ans += 1
        return ans - 1

        #m = m_steps = 0
        # for n in nums:
        #    steps = self.num_steps(n)
        #    if steps > m_steps or (steps == m_steps and n > m):
        #        m, m_steps = n, steps
        #bonus = 0
        # for n in nums:
        #    if n:
        #        bonus += 1
        #        if n != 1 and n != m and n%2 == 1:
        #            bonus += 1
        # if bonus == 0:
        #    bonus = 1
        # return m_steps + bonus - 1

    def num_steps(self, n):
        #steps = 0
        #tmp = n
        # while n:
        #    if n&1:
        #        n ^= 1
        #    else:
        #        n >>= 1
        #    steps += 1
        # return steps
        #
        if n == 0:
            return 0
        steps, mask = 0, 1
        while mask <= n:
            if n & mask:
                steps += 2
            else:
                steps += 1
            mask <<= 1
        return steps - 1
