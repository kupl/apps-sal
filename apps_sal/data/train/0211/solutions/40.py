class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 0

        def dfs(cur_pos):
            nonlocal res
            if cur_pos == len(s):
                res = max(res, len(seen))
            for next_pos in range(cur_pos, len(s)):
                if s[cur_pos:next_pos + 1] not in seen:
                    seen.add(s[cur_pos:next_pos + 1])
                    dfs(next_pos + 1)
                    seen.remove(s[cur_pos:next_pos + 1])

        seen = set()
        dfs(0)
        return res
