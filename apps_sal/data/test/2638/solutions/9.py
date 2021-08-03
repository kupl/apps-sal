class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = [0]
        for row in triangle:
            res = [row[i] + min([res[j] for j in (i - 1, i) if 0 <= j < len(res)]) for i in range(len(row))]
        return min(res)
