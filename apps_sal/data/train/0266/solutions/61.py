from collections import Counter


class Solution:

    def numSplits(self, s: str) -> int:
        hist_left = Counter(s[:1])
        hist_right = Counter(s[1:])
        count = 0
        for i in range(1, len(s)):
            v = s[i]
            if len(list(hist_left.keys())) == len(list(hist_right.keys())):
                count += 1

            hist_left[v] += 1

            if hist_right[v] == 1:
                del hist_right[v]
            else:
                hist_right[v] -= 1
        return count
