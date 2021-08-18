class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        ans = 0
        counter = collections.Counter()

        for size in range(minSize, maxSize + 1):
            for j in range(len(s) - size + 1):
                substring = s[j:j + size]
                if len(set(substring)) <= maxLetters:
                    counter[substring] += 1
                    ans = max(ans, counter[substring])
        return ans
