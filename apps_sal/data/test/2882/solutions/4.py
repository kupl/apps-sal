class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []

        def backtrack(left=0, right=0, tmp=''):
            if len(tmp) == 2 * n:
                ret.append(tmp)
                return
            if left < n:
                backtrack(left + 1, right, tmp + '(')
            if left > right:
                backtrack(left, right + 1, tmp + ')')

        backtrack()
        return ret
