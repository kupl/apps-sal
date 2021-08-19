class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.dfs(n, 0, 0, '')
        return self.res

    def dfs(self, n, left, right, path):
        if left > n or right > n:
            return
        if n == 0:
            self.res.append(path)
            return
        if left == 0:
            self.dfs(n, left + 1, right, path + '(')
        if left == right and left != 0:
            self.dfs(n - left, 0, 0, path)
        if left > right:
            self.dfs(n, left + 1, right, path + '(')
            self.dfs(n, left, right + 1, path + ')')
