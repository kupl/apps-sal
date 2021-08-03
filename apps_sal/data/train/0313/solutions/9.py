class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay)
        n = len(bloomDay)
        if m * k > n:
            return -1

        while left <= right:
            mid = (left + right) // 2
            c = 0
            bout = m
            print((left, mid, right))
            for b in bloomDay:
                if b <= mid:
                    c += 1
                else:
                    c = 0
                if c >= k:
                    bout -= 1
                    c -= k
                    if bout == 0:
                        break
            if bout == 0:
                right = mid - 1
            else:
                left = mid + 1
        return left
