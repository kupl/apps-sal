class Solution:
    def lastSubstring(self, s: str) -> str:
        slow, compareCnt, n = 0, 0, len(s)
        for fast in range(1, n):
            if s[fast] != s[slow + compareCnt] or slow + compareCnt == fast - compareCnt - 1:
                if s[fast] > s[slow + compareCnt]:
                    slow = fast if s[fast] > s[slow] else fast - compareCnt
                compareCnt = 0
            else:
                compareCnt += 1
        return s[slow:]
