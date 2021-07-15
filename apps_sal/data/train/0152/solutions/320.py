class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo, hi = 1, 10**9
        while hi>lo:
            mid = (lo+hi+1)//2
            lapo = position[0]
            co = 1
            for po in position[1:]:
                if po-lapo >= mid:
                    lapo = po
                    co += 1
            if co >= m:
                lo = mid
            else:
                hi = mid-1
        return lo
