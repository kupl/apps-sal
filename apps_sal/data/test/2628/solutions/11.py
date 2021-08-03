class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]
        mask = 0x1
        for l in range(n):
            for c in ans[::-1]:
                ans.append(mask | c)
            mask <<= 1
        return ans
