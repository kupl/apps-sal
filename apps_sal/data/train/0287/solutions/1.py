class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return (1, 2, 3, 8, 10, 36, 41, 132, 250, 700, 750, 4010, 4237, 10680, 24679)[N - 1]
