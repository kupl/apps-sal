class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        prev = -1
        best = 0
        for i in range(0, len(seats)):
            if seats[i] == 1:
                if prev == -1:
                    distance = i
                else:
                    distance = (i - prev) // 2
                best = max(best, distance)
                prev = i
        best = max(best, len(seats) - prev - 1)

        return best
