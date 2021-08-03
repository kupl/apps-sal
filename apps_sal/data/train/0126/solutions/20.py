class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if minSize > len(s):
            return 0
        left = 0
        candidates = Counter()
        while left <= len(s) - minSize:
            right = left + minSize
            count = set(s[left:right])
            while right <= len(s) and right - left <= maxSize and len(count) <= maxLetters:
                if right < len(s):
                    count.add(s[right])
                candidates[s[left:right]] += 1
                right += 1
            left += 1
        if not candidates:
            return 0
        return max(candidates.values())
