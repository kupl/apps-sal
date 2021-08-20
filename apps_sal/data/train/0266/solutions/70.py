class Solution:

    def numSplits(self, s: str) -> int:
        (cur, h) = (Counter(), Counter(s))
        cnt = 0
        for c in s:
            h[c] -= 1
            cur[c] += 1
            if h[c] == 0:
                del h[c]
            cnt += len(h) == len(cur)
        return cnt
