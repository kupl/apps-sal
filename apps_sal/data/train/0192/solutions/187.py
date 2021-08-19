class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        sorted_ = sorted(piles, key=lambda x: -x)
        answer = 0
        for i in range(len(sorted_) // 3):
            answer += sorted_[2 * i + 1]
        return answer
