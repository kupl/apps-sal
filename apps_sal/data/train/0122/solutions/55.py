class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalPoints, window = sum(cardPoints), len(cardPoints) - k
        i, j, Sum, Min = 0, 0, 0, totalPoints

        while j < len(cardPoints):
            Sum += cardPoints[j]

            if j - i + 1 > window:
                Sum -= cardPoints[i]
                i += 1

            if j - i + 1 == window:
                Min = min(Min, Sum)
            j += 1

        # print(Min)
        return totalPoints - Min
