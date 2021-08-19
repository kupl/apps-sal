class Solution:

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = []
        size = 0

        def search_tails(tails, n):
            if len(tails) == 0:
                return 0
            (l, r) = (0, len(tails))
            while l < r:
                m = (l + r) // 2
                if tails[m] < n:
                    l = m + 1
                else:
                    r = m
            return l
        for n in nums:
            i = search_tails(tails, n)
            if i == len(tails):
                tails.append(n)
            else:
                tails[i] = n
        return len(tails)
