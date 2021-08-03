'''
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        A = bloomDay
        if m * k > len(A): return -1
        left, right = 1, max(A)
        while left < right:
            mid = (left + right) // 2
            flow = bouq = 0
            for a in A:
                flow = 0 if a > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m: break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return left
'''


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        l, r = 1, max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            temp = 0
            cnt = 0
            for n in bloomDay:
                temp = 0 if n > mid else temp + 1
                if temp >= k:
                    temp = 0
                    cnt += 1
                    if cnt == m:
                        break
            if cnt == m:
                r = mid
            else:
                l = mid + 1
        return l
