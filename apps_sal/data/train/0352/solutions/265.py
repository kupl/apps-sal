class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def dfs(str):
            dep = 1
            for longer_str in words:
                if len(longer_str) == len(str) + 1:
                    for i in range(len(str) + 1):
                        new_str = longer_str[:i] + longer_str[i + 1:]
                        if new_str == str:
                            dep = max(dep, dfs(longer_str) + 1)
                            seen.append(longer_str)
            return dep

        seen = []
        depth = []
        words = sorted(words, key=len)
        for str in words:
            if str not in seen:
                depth.append(dfs(str))

        return max(depth)
