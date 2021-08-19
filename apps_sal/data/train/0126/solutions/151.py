class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        left = 0
        result = 0
        count = collections.defaultdict(int)
        occurances = collections.defaultdict(int)
        for (right, char) in enumerate(s):
            count[char] += 1
            while right - left + 1 > minSize:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            if right - left + 1 == minSize and len(count) <= maxLetters:
                occurances[s[left:right + 1]] += 1
                result = max(result, occurances[s[left:right + 1]])
        return result
