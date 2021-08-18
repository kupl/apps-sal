class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        self.piles = piles
        l, r = 1, max(piles)

        while l <= r:
            K = (l + r) // 2
            if self.eat_time(K) <= H:
                r = K - 1
            else:
                l = K + 1
        return l

    def eat_time(self, K):
        cnt = 0
        for banana in self.piles:
            q, mod = divmod(banana, K)
            cnt += q
            if mod != 0:
                cnt += 1
        return cnt
