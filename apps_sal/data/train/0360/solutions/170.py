class Solution:
    # def shipWithinDays(self, weights: List[int], D: int) -> int:
    #     if D == 1:
    #         return sum(weights)
    #     curCap = sum(weights)//D
    #     days = 1
    #     i = 0
    #     cap = curCap
    #     while i < len(weights):
    #         cap -= weights[i]
    #         if cap <= 0:
    #             days += 1
    #             if cap == 0:
    #                 i += 1
    #             cap = curCap
    #         else:
    #             i += 1
    #         if days > D:
    #             curCap += 1
    #             days = 1
    #             i = 0
    #             cap = curCap
    #     return curCap
    
    def shipWithinDays(self, weights, D):
        l, r = max(weights), sum(weights)
                            
        while l < r:
            m, days, curWeight = (l + r) // 2, 1, 0
            for weight in weights:
                if curWeight + weight > m:
                    days += 1
                    curWeight = 0
                if days > D:
                    l = m + 1
                    break
                curWeight += weight
            else: 
                r = m
        return l
    
        # def shipWithinDays(self, weights, D):
    #     left, right = max(weights), sum(weights)
    #     while left < right:
    #         mid, need, cur = (left + right) // 2, 1, 0
    #         for w in weights:
    #             if cur + w > mid:
    #                 need += 1
    #                 cur = 0
    #             cur += w
    #         if need > D: left = mid + 1
    #         else: right = mid
    #     return left

