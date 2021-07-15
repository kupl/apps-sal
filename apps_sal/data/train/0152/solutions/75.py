class Solution:
    def maxDistance(self, arr: List[int], m: int) -> int:
        arr = sorted(arr)
        small = sys.maxsize
        for a, b in zip(arr, arr[1:]):
            small = min(small, b-a)
        def count(d):
            cur = arr[0]
            res = 1
            for i in range(1, len(arr)):
                if arr[i] - cur >= d:
                    res += 1
                    cur = arr[i]
            return res >= m
        
        def bs(l, r):
            if l > r: return 0
            mid = l + (r-l)//2
            if count(mid):
                return bs(mid+1, r) or mid
            else:
                return bs(l, mid-1)
                        
        return bs(small, arr[-1]-arr[0])
        
                    

