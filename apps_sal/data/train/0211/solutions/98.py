class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # take greedy
        words = list(s)
        N = len(words)
        ans = 0

        def backtrack(words, s):
            nonlocal ans
            n = len(words)
            if n == 0:
                ans = max(len(s), ans)
            for i in range(1, n + 1):
                if str(words[:i]) not in s:
                    s.add(str(words[:i]))
                    backtrack(words[i:], s)
                    s.remove(str(words[:i]))

        backtrack(words, set())
        return ans
