class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def is_ok(piles, H, mid):
            sum = 0
            for i in range(len(piles)):
                if piles[i] <= mid:
                    sum += 1
                else:
                    sum += math.ceil(piles[i] / mid)
            return sum <= H
        
        ok = sum(piles)
        ng = 0
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(piles, H, mid):
                ok = mid
            else:
                ng = mid
        return ok
