class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited = set()
        #@lru_cache(None)
        def solve(cur: str) -> int:
            ans = 0
            if not cur:
                return 0
            for i in range(1, len(s) + 1):
                candidate = cur[:i]
                if candidate not in visited:
                    visited.add(candidate)
                    ans = max(ans, 1 + solve(cur[i:]))
                    visited.remove(candidate)
            return ans
        return solve(s)
                    
        

