class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        max_len = [1]

        def helper(i, s, vis):
            if i == len(s) and i != s:
                max_len[0] = max(max_len[0], len(vis))
                return
            j = i
            while j < len(s):
                if s[i:j + 1] not in vis and s[i:j + 1] != s:
                    vis[s[i:j + 1]] = 1
                    helper(j + 1, s, vis)
                    del vis[s[i:j + 1]]
                j += 1

        helper(0, s, {})
        return max_len[0]
