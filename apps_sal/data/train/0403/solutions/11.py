class Solution:

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tails = [-float('inf')]
        for x in nums:
            for i in range(len(tails) - 1, -1, -1):
                if x > tails[i]:
                    if i == len(tails) - 1:
                        tails.append(x)
                    else:
                        tails[i + 1] = x
                    break
            if len(tails) == 4:
                return True
        return False
