class Solution:

    def findWinner(self, res, sqlist, n, t, turn):
        if turn == 'Alice':
            if res[t] == 1:
                res[n] = 1
                return res
            if res[t] == 2:
                return res
            if res[t] == 0:
                ind = len(sqlist) - 1
                while ind >= 0:
                    temp = t - sqlist[ind]
                    if temp >= 0:
                        fw1 = Solution()
                        res = fw1.findWinner(res, sqlist, n, temp, 'Bob')
                        if res[temp] == 2:
                            res[t] = 1
                            res[n] = 1
                            return res
                    ind -= 1
                res[t] = 2
                return res
        if turn == 'Bob':
            if res[t] == 2:
                res[n] = 1
                return res
            if res[t] == 1:
                return res
            if res[t] == 0:
                ind = len(sqlist) - 1
                while ind >= 0:
                    temp = t - sqlist[ind]
                    if temp >= 0:
                        fw2 = Solution()
                        res = fw2.findWinner(res, sqlist, n, temp, 'Alice')
                        if res[temp] == 2:
                            res[t] = 1
                            res[n] = 2
                            return res
                    ind -= 1
                res[t] = 2
                return res
        return res

    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        res = []
        for i in range(n + 1):
            res.append(0)
        sqlist = []
        i = 1
        isq = 1
        while isq <= n:
            sqlist.append(isq)
            res[isq] = 1
            i += 1
            isq = i ** 2
        fw = Solution()
        finres = fw.findWinner(res, sqlist, n, n, 'Alice')
        if finres[n] == 1:
            return True
        else:
            return False
