class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible(days):
            flowers = 0
            bouquets = 0
            for bloom in bloomDay:
                if bloom<=days:
                    flowers += 1
                    if flowers>=k:
                        bouquets += 1
                        flowers = 0
                        if bouquets>=m:
                            return True
                else:
                    flowers = 0
            return False
            
        if len(bloomDay)<m*k:
            return -1
        
        l = 1
        h = max(bloomDay)
        while l<h:
            days = (l+h)//2
            if possible(days):
                h = days
            else:
                l = days+1
        return l

