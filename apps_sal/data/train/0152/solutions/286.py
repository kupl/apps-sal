class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def trial(n):
            prev, curr, ct = 0, 1, 1
            while True:
                if curr >= len(position):
                    return False
                if position[curr] - position[prev] >= n:
                    prev = curr
                    ct += 1
                if ct == m:
                    return True
                curr += 1
        
        l, r = 1, position[-1] - position[0] + 1
        ret = 0
        while l < r:
            mid = (l + r + 1) // 2
            ans = trial(mid)
            if ans:
                l = mid
            else:
                r = mid - 1
        return l
