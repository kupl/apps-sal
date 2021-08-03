class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(pos):
            placed = 1
            i = 0
            j = 1
            while j < l:
                if position[j] - position[i] >= pos:
                    placed += 1
                    if placed == m:
                        return True
                    i = j
                    j = i + 1
                else:
                    j += 1
            return (True if placed == True else False)

        l = len(position)
        mx = max(position) - min(position)
        position.sort()
        lo = 1
        hi = mx
        ans = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
