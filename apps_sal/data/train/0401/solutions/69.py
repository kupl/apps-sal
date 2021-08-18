class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        nums.sort()

        m3 = []
        m2 = []
        m1 = []

        for i in nums:
            if i % 3 == 0:
                m3.append(i)
            elif i % 3 == 2:
                m2.append(i)
            elif i % 3 == 1:
                m1.append(i)

        total = sum(nums)
        if total % 3 == 0:
            return total
        elif total % 3 == 2:
            comp1 = 0
            comp2 = 0

            if len(m2) > 0:
                comp1 = total - m2[0]

            if len(m1) > 1:
                comp2 = total - m1[0] - m1[1]

            return max(comp1, comp2)

        elif total % 3 == 1:
            comp1 = 0
            comp2 = 0

            if len(m1) > 0:
                comp1 = total - m1[0]

            if len(m2) > 1:
                comp2 = total - m2[0] - m2[1]

            return max(comp1, comp2)
