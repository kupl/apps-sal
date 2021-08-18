class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSub(s1, s2):
            it = iter(s2)
            return all(i in it for i in s1)
        keep, max1, N = False, -1, len(strs)
        mask = [True] * N
        for i in range(N):
            for j in range(N):
                if i != j and isSub(strs[i], strs[j]):
                    mask[i] = False
                    break
        for i in range(N):
            if mask[i]:
                max1 = max(max1, len(strs[i]))
        return max1
