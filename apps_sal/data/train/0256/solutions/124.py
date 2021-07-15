class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
    
#         3 6 7 11 
#         H = 8
#         sumi = 27 
#         mini = 4
#         maxi = max(piles) = 11
        
        # 1 2 3 4 5 6 7 8 10 11
        # func() => 
        # F F F T T T T T T  T 
        mini = 1
        maxi = max(piles)
        ans = 0
        while(mini<=maxi):
            mid = mini+(maxi-mini)//2
            value = sum((p-1)//mid + 1 for p in piles)
            # print(value, mid)
            if value<=H:
                ans = mid
                maxi = mid-1
            else:
                mini = mid+1
        return ans
