class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = collections.Counter()
        n = len(s)
        size = minSize
        while size <= maxSize:
            M = collections.defaultdict(int)
            for (i, c) in enumerate(s):
                if i < size:
                    M[c] += 1
                    continue
                if len(M) <= maxLetters:
                    res[s[i - size:i]] += 1
                M[s[i - size]] -= 1
                if M[s[i - size]] == 0:
                    del M[s[i - size]]
                M[c] += 1
            if len(M) <= maxLetters:
                res[s[n - size:]] += 1
            size += 1
        ans = res.most_common(1)
        if not ans:
            return 0
        else:
            return ans[0][1]
