class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = {}
        for i in range(len(s) - minSize + 1):
            word = s[i: i+minSize]
            if word in count:
                count[word] += 1
            else:
                if len(set(word)) <= maxLetters:
                    count[word] = 1
        return max(count.values()) if count else 0
