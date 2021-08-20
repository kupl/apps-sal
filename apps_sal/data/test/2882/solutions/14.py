class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []

        def genparen(prefix, opens, closes):
            if len(prefix) == 2 * n:
                results.append(prefix)
                return
            if opens < n:
                genparen(prefix + '(', opens + 1, closes)
            if closes < opens:
                genparen(prefix + ')', opens, closes + 1)
        genparen('', 0, 0)
        return results
