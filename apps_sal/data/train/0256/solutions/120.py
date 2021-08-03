class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        bananas = sum(piles)
        K = bananas // H + (bananas % H != 0)
        while True:
            if sum([pile // K + (pile % K != 0) for pile in piles]) <= H:
                return K
            K += 1
