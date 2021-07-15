class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        mini = max(weights)
        maxi = sum(weights)
        
        if len(weights) == 1:
            return weights[0]
        
        while maxi >= mini:
            mid = (maxi + mini) // 2 
            if self.check(weights, mid) < D:
                maxi = mid - 1
            elif self.check(weights, mid) > D:
                mini = mid + 1
            else:
                maxi = mid - 1
            print(mini)
        return mini
            
    def check(self, piles, num):
        res = 0
        i = 0
        count = 0
        while i < len(piles):
            if res + piles[i] < num:
                res += piles[i]
            elif res+piles[i] == num:
                res = 0
                count += 1
            else:
                res = piles[i]
                count += 1
            i += 1
        count = count if res == 0 else count + 1
        return count
