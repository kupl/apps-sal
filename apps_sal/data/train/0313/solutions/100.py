class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        '''
        binary search
        '''
        def check(day):
            adjacent = 0
            made = 0
            for f in range(len(flowers)):
                if day >= bloomDay[f]:
                    flowers[f] = True
                    adjacent += 1
                else:
                    adjacent = 0
                if adjacent>=k:
                    adjacent = 0
                    made += 1
                if made >= m:
                    return True
            return False
        
        if len(bloomDay) < m * k:
            return -1
        
        flowers = [False] * len(bloomDay)
        
        l=1
        r=max(bloomDay)
        while l<r:
            mid = l + (r - l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l
                    
                

