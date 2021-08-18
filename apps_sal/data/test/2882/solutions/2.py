class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1 or type(n) != int:
            return []
        ret = []
        tmp = []
        tmp.append({"str": "(", "cnt": 1, "rcnt": 0})
        while tmp:
            cur = tmp.pop()
            if n == cur["cnt"]:
                ret.append(cur["str"] + ')' * (n - cur["rcnt"]))
            else:
                if cur["cnt"] > cur["rcnt"]:
                    tmp.append({"str": cur["str"] + ')', "cnt": cur["cnt"], "rcnt": cur["rcnt"] + 1})
                tmp.append({"str": cur["str"] + '(', "cnt": cur["cnt"] + 1, "rcnt": cur["rcnt"]})
        return ret
