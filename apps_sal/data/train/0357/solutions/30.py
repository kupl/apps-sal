class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        dips = [0 for _ in range(n)]
        dist = n
        for i in range(n):
            if seats[i] == 1:
                dist = 0
            else:
                dips[i] = dist
            dist += 1
        print(dist, dips)
        dist = n
        minimum = 0
        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                dist = 0
            else:
                if dips[i] > dist:
                    dips[i] = dist
                if dips[i] > minimum:
                    minimum = max(minimum, dips[i])
            dist += 1
        return minimum
