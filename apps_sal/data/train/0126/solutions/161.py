class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        strcount = Counter()
        unique = set(s[:minSize])
        front = 0
        back = minSize
        while back < len(s):
            if len(unique) <= maxLetters:
                strcount[s[front:back]] = strcount.get(s[front:back], 0) + 1
            front += 1
            back += 1
            unique = set(s[front:back])
        if len(unique) <= maxLetters:
            strcount[s[front:back]] = strcount.get(s[front:back], 0) + 1
        return max(list(strcount.values()) or [0])
