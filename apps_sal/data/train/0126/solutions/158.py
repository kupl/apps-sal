class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l = 0
        r = 0
        strMap = collections.defaultdict(int)
        curr = ''
        currMap = collections.defaultdict(int)
        unique = 0
        while r < len(s):
            char = s[r]
            if currMap[char] == 0:
                unique += 1
            currMap[char] += 1
            curr += char
            while unique > maxLetters or len(curr) > minSize:
                curr = curr[1:]
                currMap[s[l]] -= 1
                if currMap[s[l]] == 0:
                    unique -= 1
                l += 1
            print(curr)
            if len(curr) >= minSize:
                strMap[curr] += 1
            r += 1
        return max(list(strMap.values()) or (0, 0))
