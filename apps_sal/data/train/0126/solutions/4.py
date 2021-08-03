class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        seen = defaultdict(lambda: 0)
        m = defaultdict(lambda: 0)
        left = 0

        for i in range(len(s)):
            m[s[i]] += 1

            while(len(m) > maxLetters or i - left + 1 > maxSize):
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    m.pop(s[left])
                left += 1

            temp = left
            while i - temp + 1 >= minSize:
                seen[s[temp:i + 1]] += 1
                temp += 1

        if not seen:
            return 0
        return max(list(seen.values()))
