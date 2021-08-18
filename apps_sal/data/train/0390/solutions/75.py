class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        s = [i**2 for i in range(1, int(n**(1 / 2)) + 1)]
        record = {}

        def helper(i):
            if i in record:
                return record[i]
            if i == 0:
                return False
            for j in s:
                if j > i:
                    record[i] = False
                    return False
                if not helper(i - j):
                    record[i] = True
                    return True

        res = helper(n)
        return res
