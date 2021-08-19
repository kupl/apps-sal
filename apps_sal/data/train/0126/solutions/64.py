class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # sliding window
        res = collections.Counter()
        n = len(s)
        size = minSize
        while size <= maxSize:
            M = collections.defaultdict(int)
            for i, c in enumerate(s):
                if i < size:
                    M[c] += 1
                    continue

                if len(M) <= maxLetters:
                    res[s[i - size:i]] += 1

                # slide the window
                M[s[i - size]] -= 1
                if M[s[i - size]] == 0:
                    del M[s[i - size]]
                M[c] += 1
            # check for last one
            if len(M) <= maxLetters:
                res[s[n - size:]] += 1

            size += 1

        # print(res.most_common(1))
        ans = res.most_common(1)
        if not ans:
            return 0
        else:
            return ans[0][1]
