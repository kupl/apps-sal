class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        w = n - k
        left, right = 0, w - 1
        ans = float('-inf')

        win_sum = sum(cardPoints[:w])
        total = sum(cardPoints)
        while right < n:
            sub = total - win_sum
            ans = max(sub, ans)
            if left < n:
                win_sum -= cardPoints[left]
            left += 1
            right += 1
            if right < n:
                win_sum += cardPoints[right]

        return ans
