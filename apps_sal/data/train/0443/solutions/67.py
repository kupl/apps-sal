class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0

        def dfs(i: int, cur_len: int, last_elem: int, flag: str):
            nonlocal result
            if cur_len == 3:
                result += 1
                return

            for x in range(i, len(rating)):
                if flag == 'l':
                    if rating[x] > last_elem:
                        dfs(x + 1, cur_len + 1, rating[x], 'l')
                elif flag == 's':
                    if rating[x] < last_elem:
                        dfs(x + 1, cur_len + 1, rating[x], 's')

        for i in range(len(rating) - 1):
            dfs(i + 1, 1, rating[i], 'l')
            dfs(i + 1, 1, rating[i], 's')
        return result
