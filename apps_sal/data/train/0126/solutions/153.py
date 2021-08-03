class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l = 0
        r = 0
        strMap = collections.defaultdict(int)
        curr = ''
        currMap = collections.defaultdict(int)
        while r < len(s):
            char = s[r]
            currMap[char] += 1
            curr += char
            while len(currMap) > maxLetters or len(curr) > minSize:
                curr = curr[1:]
                currMap[s[l]] -= 1
                if currMap[s[l]] == 0:
                    del currMap[s[l]]
                l += 1
            if len(curr) == minSize:
                strMap[curr] += 1
            r += 1
        return max(strMap.values()) if strMap else 0
