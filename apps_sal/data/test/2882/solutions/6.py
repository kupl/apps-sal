class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = set()
        if n == 0:
            result = ['']
        else:
            for i in range(1, n + 1):
                temp1 = {'(' + x + ')' for x in self.generateParenthesis(i - 1)}
                temp2 = {x for x in self.generateParenthesis(n - i)}
                temp = {x + y for x in temp1 for y in temp2} | {x + y for x in temp2 for y in temp1}
                result = result | temp
            result = sorted(list(result))
        return result
