class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        feq = collections.Counter()

        N = len(s)
        for i in range(N):
            letters = set([c for c in s[i: i + minSize - 1]])
            for j in range(minSize, maxSize + 1):
                k = i + j
                if k > N:
                    break
                letters.add(s[k - 1])
                if len(letters) > maxLetters:
                    break
                feq[s[i:k]] += 1

        return max(feq.values()) if list(feq.values()) else 0
