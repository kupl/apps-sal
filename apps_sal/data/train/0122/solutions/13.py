class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        if n == k or n < k:
            return total
        remove = n - k
        ans = 0
        'memo = [0]*(n+1)\n        memo[0] = 0\n        \n        start = 0\n        for i in range(0, n):\n            memo[i+1] = memo[i] + cardPoints[i]            \n            if i-start + 1 == remove: \n                ans = max(ans, total-(memo[i+1]-memo[start]))\n                start = start+1'
        curr = 0
        start = 0
        for right in range(n):
            curr += cardPoints[right]
            if right - start + 1 == remove:
                ans = max(ans, total - curr)
                curr -= cardPoints[start]
                start += 1
        return ans
