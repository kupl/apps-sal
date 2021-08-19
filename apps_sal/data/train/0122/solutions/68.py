# O(n) time and O(1) space
# alternative dp solution O(k) space: form two k sized arrays: 1 to k and n-k to n
# https://www.youtube.com/watch?v=t3JHx5J01F0 9mins06s
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr_max = sum(cardPoints[:k])
        ans = curr_max
        for i in range(1, k + 1):
            curr_max += cardPoints[-i] - cardPoints[k - i]
            ans = max(ans, curr_max)
        return ans
