class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        answer = 0
        while len(piles) > 0:
            largest = piles.pop()
            almostLargest = piles.pop()
            smallest = piles.pop(0)
            answer += almostLargest
        return answer
