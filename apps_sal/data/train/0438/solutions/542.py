import bisect

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        s = [0, n + 1]
        
        if n == m: return n
        
        for i, x in enumerate(reversed(arr)):
            j = bisect.bisect_right(s, x)
            s.insert(j, x)
            if m == x - s[j-1] - 1 or m == s[j + 1] - x - 1:
                return n - i - 1
            
        return -1
