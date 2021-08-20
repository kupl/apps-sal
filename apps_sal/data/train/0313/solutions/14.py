class Solution:

    def minDays(self, F: List[int], m: int, k: int) -> int:
        if m * k > len(F):
            return -1
        ans = 0
        left = 1
        right = max(F)
        while left <= right:
            mid = (left + right) // 2
            if self.possible(mid, F, m, k) == True:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def possible(self, mid, F, m, k):
        count = 0
        a = 0
        for i in range(len(F)):
            if a == k:
                count += 1
                a = 0
            if F[i] <= mid:
                a += 1
            else:
                a = 0
        if a == k:
            count += 1
        if count >= m:
            return True
        return False
