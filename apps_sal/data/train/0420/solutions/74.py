from collections import defaultdict
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = 0
        vowel_map = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        visited = {0: -1}
        pattern = 0
        for i, c in enumerate(s):
            if c in vowel_map:
                pattern ^= 1 << vowel_map[c]
            if pattern not in visited:
                visited[pattern] = i
            
            res = max(res, i-visited[pattern])
        return res

