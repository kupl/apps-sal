class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 0, position[-1] - position[0] + 1

        def c(x):
            y = m
            y -= 1
            last = 0
            j = 0
            for _ in range(y):
                while j < len(position) and position[j] - position[last] < x:
                    j += 1
                if j == len(position):
                    return 0
                last = j
            return 1

        while l < r:
            mid = (r + l) // 2
            dist = c(mid)
            if not dist:
                r = mid
            else:
                l = mid + 1
        return l - 1
