class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        s = ''
        self.dfs(stack, 0, 0, s, n)
        return stack

    def dfs(self, stack, first, last, s, n):
        if last == n:
            stack.append(s)
        else:
            if first < n:
                self.dfs(stack, first + 1, last, s + '(', n)
            if last < first:
                self.dfs(stack, first, last + 1, s + ')', n)
