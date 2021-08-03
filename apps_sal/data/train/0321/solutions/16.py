class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        size_t = len(s1)

        for idx in range(size_t):
            if s1[idx] == s2[idx]:
                continue
            elif s1[idx] < s2[idx]:
                ans = set(map(lambda x, y: x <= y, s1, s2))
                break
            else:
                ans = set(map(lambda x, y: x >= y, s1, s2))
                break

        if len(ans) > 1:
            return False
        return True
