class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(s, start, seen):
            ans = 0
            for end in range(start + 1, len(s) + 1):
                added = s[start:end]
                print(added)
                if added not in seen:
                    seen.add(added)
                    ans = max(ans, 1 + helper(s, end, seen))
                    seen.remove(added)

            return ans
        seen = set()
        return helper(s, 0, seen)
