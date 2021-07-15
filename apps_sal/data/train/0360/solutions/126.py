class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        end = sum(weights)
        start = end // D
        
        while start < end:
            mid = (start + end) // 2
            # print(start, end, mid)
            
            days = 1
            curr_sum = 0
            for i in range(len(weights)):
                if weights[i] > mid:
                    days = D + 1
                    break
                if curr_sum + weights[i] > mid:
                    days += 1
                    if days > D:
                        break
                    curr_sum = weights[i]
                else:
                    curr_sum += weights[i]
            # print(days)
            
            if start == mid:
                if days > D:
                    return end
                else:
                    return start
                
            if days > D:
                start = mid
            else:
                end = mid
        return start
