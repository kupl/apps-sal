class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        cache=Counter(A)
        c_list=sorted(list(cache),key=abs)
        for x in c_list:
            if cache[x]>cache[2*x]:
                return False
            cache[2*x]-=cache[x]
        return True
