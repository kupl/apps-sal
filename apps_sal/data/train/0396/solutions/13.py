class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        res=1
        visited=set()
        while res<K:
            res=10*res+1
        d=res%K
        while d>0:
            if d not in visited:
                visited.add(d)
                res=10*res+1
                d=(10*d+1)%K
            else:
                return -1
        return len(str(res))
