class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        m0 = 0
        m1 = 0
        m2 = 0
        for n in nums:
            m = n % 3
            (m0n, m1n, m2n) = (m0, m1, m2)
            if m == 0:
                m0n = m0 + n
                m1n = m1 + n
                m2n = m2 + n
            elif m == 1:
                if m2 % 3 == 2:
                    m0n = max(m0, m2 + n)
                m1n = max(m1, m0 + n)
                if m1 % 3 == 1:
                    m2n = max(m2, m1 + n)
            elif m == 2:
                if m1 % 3 == 1:
                    m0n = max(m0, m1 + n)
                if m2 % 3 == 2:
                    m1n = max(m1, m2 + n)
                m2n = max(m2, m0 + n)
            (m0, m1, m2) = (m0n, m1n, m2n)
        return m0
