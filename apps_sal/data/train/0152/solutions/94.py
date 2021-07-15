class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        mx = position[-1]
        lo, hi = 1, mx

        def judge(x):
            pre, cnt = -mx, 0
            for p in position:
                if p - pre >= x:
                    pre = p
                    cnt += 1
                if cnt >= m:
                    return True
            return False

        while lo <= hi:
            mid = (lo+hi)//2
            if judge(mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
