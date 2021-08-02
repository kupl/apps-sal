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
                genparen(prefix + "(", opens + 1, closes)
            if closes < opens:
                genparen(prefix + ")", opens, closes + 1)

        genparen('', 0, 0)
        return results


#         paren_map = {}
#         paren_map[1] = set(["()"])

#         for i in range(2, n+1):
#             paren_map[i] = self.generate_parens(paren_map[i-1])

#         return list(paren_map[n])


#     def generate_parens(self, st):
#         result = set()

#         for elem in st:
#             for i in range(len(elem)):
#                 candidate = elem[:i] + "()" + elem[i:]
#                 result.add(candidate)

#         return result
