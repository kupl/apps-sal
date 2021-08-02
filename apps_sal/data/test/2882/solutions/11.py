class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]
        results = []

        for i in range(1, 2 * n, 2):
            first = self.generateParenthesis(int((i - 1) / 2))
            second = self.generateParenthesis(int((2 * n - i - 1) / 2))
            results += ["(" + u + ")" + v for u in first for v in second]
        return results
