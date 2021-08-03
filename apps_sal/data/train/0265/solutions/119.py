class Solution:
    def maxNonOverlapping(self, lis: List[int], tar: int) -> int:
        n = len(lis)
        pre = [0] * (n + 1)
        ans = 0
        for i in range(n):
            pre[i + 1] = pre[i] + lis[i]
        d = {0: 0}
        for i in range(1, n + 1):
            cur = pre[i]
            prev = cur - tar
            if prev in d:
                ans += 1
                d = {}
            d[cur] = 1
        return ans
