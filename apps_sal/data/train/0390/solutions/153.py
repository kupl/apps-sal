class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dic =dict()
        dic[1] = True
        dic[2] = False
        dic[3] = True
        dic[4] = True
        def helper(n):
            if n in dic:
                return dic[n]
            i = int(n ** 0.5)
            while i >= 1:
                if not helper(n - i**2):
                    dic[n] = True
                    return True
                i -=1
            dic[n] = False
            return False
        return helper(n)
