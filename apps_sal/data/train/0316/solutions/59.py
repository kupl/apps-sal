class Solution:
    def longestPrefix(self, s: str) -> str:
        # https://leetcode.com/problems/longest-happy-prefix/discuss/547237/JavaPython-Rolling-Hash
        # https://leetcode.com/problems/longest-happy-prefix/discuss/547446/C%2B%2BJava-with-picture-incremental-hash-and-KMP
        n = len(s)
        prefix = [0]*n
        j, i = 0, 1
        while i < n:
            if s[j] == s[i]:
                j += 1
                prefix[i] = j
            elif j > 0:
                j = prefix[j-1]
                i -= 1
            i += 1
        return s[:j]
