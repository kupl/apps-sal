class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if self.validBouquets(bloomDay, mid, m, k):
                right = mid
            else:
                left = mid + 1
        return left
    
    def validBouquets(self, bloomDay, days, m, k):
        # Count how many bouquets we can collect
        count_bouquets = 0
        temp_flowers = 0
        for bloom in bloomDay:
            if bloom <= days:
                temp_flowers += 1
            else:
                temp_flowers = 0
            # Determine whether flowers in hand can form a bouquet
            if temp_flowers >= k:
                count_bouquets += 1
                temp_flowers = 0
                if count_bouquets == m:
                    return True
        return False
