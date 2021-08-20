class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[:k])
        if k == len(cardPoints):
            return total
        max_sum = total
        print(max_sum)
        for i in range(k - 1, -1, -1):
            total = total + cardPoints[i - k] - cardPoints[i]
            print((i - k, total, cardPoints[i - k], cardPoints[i]))
            if total > max_sum:
                max_sum = total
        return max_sum
