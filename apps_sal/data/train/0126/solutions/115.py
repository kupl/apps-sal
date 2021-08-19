class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        i = numUnique = 0
        N = len(s)
        count = collections.defaultdict(int)
        seen = collections.defaultdict(int)
        ans = 0
        for i in range(N):
            count = collections.defaultdict(int)
            numUnique = 0
            power = 1
            hash = 0
            for j in range(i, min(i + 26, N)):
                count[s[j]] += 1
                if count[s[j]] == 1:
                    numUnique += 1
                add = (ord(s[j]) - ord('a') + 1) * 27 ** power
                hash += add
                power += 1
                if numUnique > maxLetters or j - i + 1 > maxSize:
                    break
                if minSize <= j - i + 1 <= maxSize and numUnique <= maxLetters:
                    seen[hash] += 1
                    ans = max(ans, seen[hash])
        return ans
