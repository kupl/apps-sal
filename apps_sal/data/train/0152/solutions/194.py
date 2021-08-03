class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def num(dist):
            count = 1
            curr = position[0]
            for i in range(1, n):
                if position[i] - curr >= dist:
                    count += 1
                    curr = position[i]
            return count

        start = 0
        end = position[-1] - position[0]
        res = 0
        while start < end:
            mid = (start + end) // 2
            if num(mid) >= m:
                start = mid + 1
                res = mid
            else:
                end = mid
        if num(start) >= m:
            return start
        else:
            return start - 1
