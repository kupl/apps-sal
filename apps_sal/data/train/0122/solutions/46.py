class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pre = [cardPoints[0]]
        n = len(cardPoints)
        for i in range(1, n):
            pre.append(pre[-1] + cardPoints[i])

        if k == n:
            return pre[-1]

        s = pre[-1]
        cur_s = pre[n - k - 1]
        l = 0
        r = n - k + l - 1
        ans = s - pre[n - k - 1]

        while l != len(cardPoints) - (n - k):
            cur_s -= cardPoints[l]
            l += 1
            r += 1
            cur_s += cardPoints[r]
            ans = max(ans, s - cur_s)

        return ans
