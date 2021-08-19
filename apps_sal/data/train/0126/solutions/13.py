class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = defaultdict(lambda: 0)
        m = ''
        uniques = defaultdict(lambda: set())
        n = len(s)
        for i in range(n - minSize + 1):
            end = i + minSize
            unique = set(s[i:end])
            while end <= n:
                unique.add(s[end - 1])
                if len(unique) > maxLetters:
                    break
                cur = s[i:end]
                freq[cur] += 1
                if freq[cur] > freq[m]:
                    m = cur
                end += 1
        return freq[m]
