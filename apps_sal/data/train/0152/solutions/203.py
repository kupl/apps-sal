class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def check(threshold):
            last = position[0]
            count = 1
            for p in position[1:]:
                if p - last >= threshold:
                    count += 1
                    last = p
                if count == m:
                    return True
            return False
        position.sort()
        (l, r) = (1, position[-1] - position[0])
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
