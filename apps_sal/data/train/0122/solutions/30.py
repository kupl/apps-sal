class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        total = sum(cardPoints)
        if k == length:
            return total
        curr = 0
        temp = 2 ** 31 - 1
        left = 0
        for right in range(length):
            curr += cardPoints[right]
            if right - left + 1 < length - k:
                continue
            print(right, curr)
            temp = min(temp, curr)
            curr -= cardPoints[left]
            left += 1

        return total - temp
