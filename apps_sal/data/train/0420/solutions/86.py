class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        d = {(0, 0, 0, 0, 0): -1}
        count = [0, 0, 0, 0, 0]
        pos = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        ans = 0
        for (i, char) in enumerate(s):
            if char in pos:
                count[pos[char]] = (count[pos[char]] + 1) % 2
            t = tuple(count)
            if t in d:
                ans = max(ans, i - d[t])
            else:
                d[t] = i
        return ans
