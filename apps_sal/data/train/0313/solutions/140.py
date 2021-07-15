class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canCreate(days):
            flowers = [1 if days >= bloom else 0 for bloom in bloomDay]
            bouquets = 0
            adj = 0
            for flower in flowers:
                if not flower:
                    adj = 0
                    continue
                adj += 1
                if adj == k:
                    adj = 0
                    bouquets += 1
                    if bouquets == m:
                        return True
            return False
        MAX = 10**9+1
        left, right = 1, MAX
        while left < right:
            mid = (left+right)//2
            if canCreate(mid):
                right = mid
            else:
                left = mid+1
        return left if left != MAX else -1
