class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # sum of points from left most
        # sum of points from right most
        # sum of points from both left and right

        # defualt max_sum
        total = sum(cardPoints[:k])

        # if k == len(cardPoitns), result is the total sum of cardPoints
        if k == len(cardPoints):
            return total
        max_sum = total
        print(max_sum)

        # compute sum from left to right
        for i in range(k - 1, -1, -1):
            total = total + cardPoints[i - k] - cardPoints[i]
            print((i - k, total, cardPoints[i - k], cardPoints[i]))
            if total > max_sum:
                max_sum = total
        return max_sum
