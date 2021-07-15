class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        vals = list(set(bloomDay))
        vals.sort()
        
        def invalid(threshold):
            cur = 0
            bouquets = 0
            for x in bloomDay:
                if x <= threshold:
                    cur += 1
                else:
                    bouquets += cur // k
                    cur = 0
            bouquets += cur // k
            return bouquets < m
        
        left, right = 0, len(vals) - 1
        while left <= right:
            mid = (left + right) // 2
            # print(left, right, mid)
            if invalid(vals[mid]):
                left = mid + 1
            else:
                right = mid - 1
        return vals[left]
