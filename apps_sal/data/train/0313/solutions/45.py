class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if k * m > n:
            return -1
        l, r = 1, max(bloomDay)
        ans = -1
        while l <= r:
            mid = int((l + r) / 2)
            bouquetCount = 0
            adjacentFlowerCount = 0
            for bloom in bloomDay:
                if bloom <= mid:
                    adjacentFlowerCount += 1
                    if adjacentFlowerCount == k:
                        bouquetCount += 1
                        adjacentFlowerCount = 0
                        if bouquetCount == m:
                            break
                else:
                    adjacentFlowerCount = 0
            if bouquetCount == m:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
