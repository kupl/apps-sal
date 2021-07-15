class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        hlim = sum(weights)
        llim = max(weights)
        def isValid(cap, days):
            temp = 0
            x = 0
            while x < len(weights):
                temp += weights[x]
                if temp > cap:
                    x -= 1
                    temp = 0
                    days -= 1
                x += 1
            return days >= 1
        ans = -1
        while llim <= hlim:
            mid = (llim+hlim)//2
            if isValid(mid, D):
                ans = mid
                hlim = mid-1
            else:
                llim = mid+1
        return ans
