class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        last = None
        res = 0
        for i in range(n):
            if seats[i] == 1:
                if last is not None:
                    res = max(res, (i - last) // 2)
                else:
                    res = i
                last = i
        return max(res, n - 1 - last)
