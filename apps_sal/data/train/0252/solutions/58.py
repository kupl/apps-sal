class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        if n == 0:
            return 0
        
        steps = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            for j in range(left, right+1):
                steps[j] = right
        
        #print(steps)
        res = 1
        prev = 0
        cur = steps[0]
        while cur > prev:
            if cur == n:
                return res
            
            tmp = cur
            for i in range(prev+1, cur+1):
                cur = max(cur, steps[i])
            
            prev = tmp
            res += 1
        
        return -1

