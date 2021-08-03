class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        left = 0
        right = 0
        _dict = defaultdict(int)
        _dict2 = defaultdict(int)

        while right < len(s):
            _dict[s[right]] += 1

            while len(_dict) > maxLetters or right - left + 1 > maxSize or right - left + 1 > minSize:
                _dict[s[left]] -= 1
                if _dict[s[left]] == 0:
                    del(_dict[s[left]])
                left += 1
            if len(_dict) <= maxLetters and minSize <= right - left + 1 <= maxSize:
                _dict2[s[left:right + 1]] += 1

            right += 1

        if len(_dict2) == 0:
            return 0

        return max(_dict2.values())
