class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        arr = sorted(position)
        if m == 2:
            return arr[-1] - arr[0]
        
        def check(n):
            cnt = 2
            pre = arr[0]
            for i in range(1, len(arr) - 1):
                if arr[i] - pre >= n:
                    pre = arr[i]
                    cnt += 1
                    if cnt == m:
                        break
            return cnt == m and arr[-1] - pre >= n
        
        lo, hi = 1, arr[-1] - arr[0]
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi - 1
        return hi
