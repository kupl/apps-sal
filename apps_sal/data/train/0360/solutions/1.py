class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def checkCapacity(cap: int, weights: List[int], D: int):
            val = 0
            res = 1
            for w in weights:
                val += w
                if val > cap:
                    res += 1
                    val = w
            return res <= D
        low = max(weights)
        high = min(sum(weights), low * len(weights) // D)
        while low < high:
            mid = (low + high) // 2
            if checkCapacity(mid, weights, D):
                high = mid
            else:
                low = mid + 1
        return high
