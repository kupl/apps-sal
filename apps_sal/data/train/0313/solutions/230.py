class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if not bloomDay :return -1
        if k * m > len(bloomDay): return -1

        def check(cur):
            res = 0
            curk = 0
            for item in bloomDay:
                if item <= cur:
                    curk += 1
                    if curk == k:
                        res+=1
                        curk = 0
                else:
                    curk = 0
            if res < m: return False
            return True

        b = min(bloomDay)
        e = max(bloomDay) 
        rt = 0
        #n2
        while b <= e:
            
            mid = b + (e-b)//2
            if check(mid):
                e = mid-1
            else:
                b = mid +1
        return b
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #arr = [abs difference prev and cur]
#         # for idx, val in enumerate(bloomDay):
#         h = defaultdict(list)
#         for idx, val in enumerate(bloomDay):
            
#             dif = abs(bloomday[idx+1] - val)
#             h[dif].append((idx, idx+1))
            
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        return rt

