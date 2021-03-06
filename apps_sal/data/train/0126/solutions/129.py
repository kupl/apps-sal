class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        substr = collections.Counter()
        counter = [collections.Counter(s[:minSize])]
        if len(counter[-1]) <= maxLetters:
            substr[s[:minSize]] += 1
        for i in range(1, maxSize - minSize + 1):
            counter.append(collections.Counter(counter[-1]))
            counter[-1][s[minSize + i - 1]] += 1
            if len(counter[-1]) <= maxLetters:
                substr[s[:minSize + i]] += 1
        for i in range(minSize, n):
            l = i - minSize
            for (j, cnt) in enumerate(counter):
                r = i + j
                if r >= n:
                    break
                cnt[s[l]] -= 1
                cnt[s[r]] += 1
                if cnt[s[l]] == 0:
                    cnt.pop(s[l])
                if len(cnt) <= maxLetters:
                    substr[s[l + 1:r + 1]] += 1
        return max(substr.values(), default=0)
