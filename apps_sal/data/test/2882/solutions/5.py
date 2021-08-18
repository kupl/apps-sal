class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def gen(n, open_par, res, res_set):
            print(res)
            if len(res) == 2 * n:
                res_set.append(''.join(res))
                return
            if 2 * n - len(res) > open_par:
                res.append('(')
                gen(n, open_par + 1, res, res_set)
                res.pop()
            if open_par > 0:
                res.append(')')
                gen(n, open_par - 1, res, res_set)
                res.pop()
        res_set = []
        gen(n, 0, [], res_set)
        return res_set
