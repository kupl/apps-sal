class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        res += self.increse_dfs(rating, [], 0)
        res += self.decrese_dfs(rating, [], 0)

        return res

    def increse_dfs(self, rating: List[int], tmp: List[int], res: int) -> int:
        if len(tmp) == 3:
            res += 1
            return res
        if len(rating) == 0:
            return res

        for idx, n in enumerate(rating):
            if len(tmp) == 0:
                tmp.append(n)
                res = self.increse_dfs(rating[idx + 1:], tmp, res)
                tmp.pop()
            else:
                if n > tmp[-1]:
                    tmp.append(n)
                    res = self.increse_dfs(rating[idx + 1:], tmp, res)
                    tmp.pop()
        return res

    def decrese_dfs(self, rating: List[int], tmp: List[int], res: int) -> int:
        if len(tmp) == 3:
            res += 1
            return res
        if len(rating) == 0:
            return res

        for idx, n in enumerate(rating):
            if len(tmp) == 0:
                tmp.append(n)
                res = self.decrese_dfs(rating[idx + 1:], tmp, res)
                tmp.pop()
            else:
                if n < tmp[-1]:
                    tmp.append(n)
                    res = self.decrese_dfs(rating[idx + 1:], tmp, res)
                    tmp.pop()

        return res
