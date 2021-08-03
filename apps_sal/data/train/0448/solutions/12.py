class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        P = [0]
        for x in nums:
            v = P[-1] + x
            if k:
                v %= abs(k)
            P.append(v)

        seen = set()
        for i in range(len(P) - 3, -1, -1):
            seen.add(P[i + 2])
            if P[i] in seen:
                return True
        return False
