class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        def dfs(start, seen):
            ans = 0
            if start == n:
                return ans

            for end in range(start + 1, n + 1):
                word = s[start:end]

                if word in seen:
                    continue

                seen.add(word)
                ans = max(ans, 1 + dfs(end, seen))
                seen.discard(word)

            return ans 
            
        return dfs(0, set())
