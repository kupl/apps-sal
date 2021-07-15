class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cache = {}
        
        for x in arr:
            if x%k:
                comple = k - (x%k)
            else:
                comple = 0
            if cache.get(comple,0):
                cache[comple] -=1
            else:
                if x%k in cache:
                    cache[x%k] += 1
                else:
                    cache[x%k] = 1
        return not sum(cache.values())
