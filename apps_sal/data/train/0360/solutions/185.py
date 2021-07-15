class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if self.condition(mid, weights) <= D:
                right = mid
            else:
                left = mid+1
        return left
    
    def condition(self, k, weights):
        d = 0
        cur_weight = 0
        for weight in weights:
            if cur_weight + weight == k:
                d += 1
                cur_weight = 0
            elif cur_weight + weight > k:
                d += 1
                cur_weight = weight
            else:
                cur_weight += weight
        return d+1 if cur_weight > 0 else d
        '''def count_days(k, w):
            curr_wt = 0
            count = 0
            for x in weights:
                if curr_wt+x > k:
                    count = count+1
                    cur_wt = x
                elif curr_wt+x==k:
                    count=count+1
                    curr_wt = 0
                else:
                    curr_wt = curr_wt+x
            if curr_wt > 0: return count+1
            else: return count
                
        
        l = max(weights)
        r = sum(weights)
        while l<r:
            mid = l+((r-l)//2)
            if count_days(mid, weights) <= D:
                r = mid
            else:
                l = mid+1
        return l'''
        

