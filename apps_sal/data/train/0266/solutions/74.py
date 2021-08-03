class Solution:
    def numSplits(self, s: str) -> int:
        p, q, ans = Counter(), Counter(s), 0
        for c in s[:-1]:
            p[c] += 1
            q[c] -= 1
            if not q[c]:
                del q[c]
            ans += len(p) == len(q)
        return ans
