class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        cache=dict()
        for a in A:
            cache[a]=cache.get(a,0)+1
        while len(cache)>0:
            temp=[abs(k) for k in cache.keys()]
            curr=min(temp)
            if curr==0:
                if cache[0]%2>0:
                    return False
                else:
                    cache.pop(0)
            else:
                if curr in cache:
                    if cache[curr]==0:
                        cache.pop(curr)
                    elif (2*curr not in cache) or cache[2*curr]<cache[curr]:
                        return False
                    else:
                        cache[2*curr]-=cache[curr]
                        cache.pop(curr)
                if -curr in cache:
                    if cache[-curr]==0:
                        cache.pop(-curr)
                    elif (-2*curr not in cache) or cache[-2*curr]<cache[-curr]:
                        return False
                    else:
                        cache[-2*curr]-=cache[-curr]
                        cache.pop(-curr)
        return True
