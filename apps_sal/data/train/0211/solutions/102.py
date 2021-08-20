class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        ans = 0
        for pat in range(1 << n - 1):
            start = 0
            end = 1
            split = []
            for b in bin(pat)[2:].zfill(n - 1):
                if b == '1':
                    split.append(s[start:end])
                    start = end
                    end += 1
                else:
                    end += 1
            split.append(s[start:end])
            if len(set(split)) == len(split):
                ans = max(ans, len(split))
        return ans
