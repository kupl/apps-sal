class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # @lru_cache(None)
        cache = {}
        def f(i):
            if i in cache:
                return cache[i]
            left = True
            right = True
            ret = 1
            for step in range(1,d+1):
                m = i - step
                if 0 <= m < len(arr) and arr[m] < arr[i] and left:
                    ret = max(ret,f(m)+1)
                else:
                    left = False
                m = i + step
                if 0 <= m < len(arr) and arr[m] < arr[i] and right:
                    ret = max(ret,f(m)+1)
                else:
                    right = False
                
                if (not left) and (not right):
                    break
            cache[i] = ret
            return ret
       
        mm = 0
        for i in range(len(arr)):
            fi = f(i) if i not in cache else cache[i]
            mm = max(f(i),mm)
        
        return mm

