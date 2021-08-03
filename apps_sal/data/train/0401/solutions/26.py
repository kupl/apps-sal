class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        counts = [0, 0, 0]
        small_two = []
        small_one = []

        result = 0
        for i in nums:
            result += i
            rem = i % 3
            counts[i % 3] += 1

            if rem == 0:
                continue
            elif rem == 1:
                small_one = sorted(small_one + [i])[:3]
            else:
                small_two = sorted(small_two + [i])[:3]

        # compensate
        print(small_two, small_one, result)
        if result % 3 == 2:
            return result - (small_two[0] if len(small_one) < 2 or (small_two[0] < small_one[0] + small_one[1]) else small_one[0] + small_one[1])
        if result % 3 == 1:
            return result - (small_one[0] if len(small_two) < 2 or (small_one[0] < small_two[0] + small_two[1]) else small_two[0] + small_two[1])

        return result
