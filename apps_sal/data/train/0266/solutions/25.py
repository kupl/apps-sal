class Solution:

    def numSplits(self, s: str) -> int:
        N = len(s)
        left = [0] * (N + 1)
        seen = set()
        for i in range(1, N + 1):
            c = s[i - 1]
            if c not in seen:
                left[i] = left[i - 1] + 1
                seen.add(c)
            else:
                left[i] = left[i - 1]
        right = [0] * (N + 1)
        seen.clear()
        for i in range(N - 1, -1, -1):
            c = s[i]
            if c not in seen:
                right[i] = right[i + 1] + 1
                seen.add(c)
            else:
                right[i] = right[i + 1]
        good = 0
        for i in range(N + 1):
            if left[i] == right[i]:
                good += 1
        return good
