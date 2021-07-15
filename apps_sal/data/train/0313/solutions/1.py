class Solution:
    def minDays(self, arr: List[int], m: int, k: int) -> int:
        def count(arr, x, k):
            out = 0
            count = 0
            for i in arr:
                if i <= x:
                    count += 1
                    if count == k:
                        out += 1
                        count = 0
                else:
                    count = 0

            return out
        
        if len(arr) < m*k:
            return -1
        res = -1
        bi = list(sorted(set(arr)))
        start = 0
        end = len(bi)-1
        while start <= end:
            mid = (start+end)//2
            if count(arr, bi[mid], k) >= m:
                res = bi[mid]
                end = mid - 1
            else:
                start = mid + 1

        return res

