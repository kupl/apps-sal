class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = []
        right = []
        n = len(seats)
        leftlast = None
        rightlast = None
        for i in range(n):
            if seats[i] == 1:
                left.append(0)
                leftlast = i
            else:
                if leftlast is None:
                    left.append(float('inf'))
                else:
                    left.append(i - leftlast)
            if seats[n - i - 1] == 1:
                right.append(0)
                rightlast = n - i - 1
            else:
                if rightlast is None:
                    right.append(float('inf'))
                else:
                    right.append(rightlast - n + i + 1)

        res = 0
        for i in range(n):
            res = max(res, min(right[n - i - 1], left[i]))
        return res
