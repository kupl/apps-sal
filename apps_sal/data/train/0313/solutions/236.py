class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):   #要形成至少需要的花朵数
            return -1
        l, r = 1, max(bloomDay)
        while l < r:
            mid = (l+r)//2
            flow = bouq = 0
            for a in bloomDay:
                if a > mid:
                    flow=0
                else:
                    flow+=1
                if flow== k:
                    flow = 0
                    bouq += 1
            if bouq>=m:
                r = mid
            else:
                l = mid + 1
        return l
