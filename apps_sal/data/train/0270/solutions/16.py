class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def helper(cur, tmp):
            if len(cur) == n:
                res.append(cur)
                return
            for t in tmp:
                new = [i for i in ['a', 'b', 'c'] if i != t]
                helper(cur + t, new)
        helper('', ['a', 'b', 'c'])
        return res[k - 1] if k - 1 < len(res) else ''
