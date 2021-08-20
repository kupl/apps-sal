class Solution:

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s3 = -2 ** 64 - 1
        maxset = []
        for i in reversed(nums):
            if i < s3:
                return True
            else:
                while len(maxset) > 0 and i > maxset[-1]:
                    s3 = maxset.pop(-1)
            maxset.append(i)
        return False
