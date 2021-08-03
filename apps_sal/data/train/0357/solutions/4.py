class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        N = len(seats)

        left = [0 for _ in range(N)]
        right = [0 for _ in range(N)]

        for i in range(N):

            if seats[i] == 1:
                left[i] = i
                continue

            if i == 0:
                left[i] = -1
                continue

            left[i] = left[i - 1]

        for i in range(N - 1, -1, -1):

            if seats[i] == 1:
                right[i] = i
                continue

            if i == (N - 1):
                right[i] = -1
                continue

            right[i] = right[i + 1]

        print((right, left))
        maxDistance = 0

        for pos in range(N):

            if seats[pos] == 0:
                if left[pos] == -1 or right[pos] == -1:
                    if left[pos] == -1:
                        distance = right[pos] - pos
                    else:
                        distance = pos - left[pos]
                else:
                    distance = min(right[pos] - pos, pos - left[pos])

                maxDistance = max(maxDistance, distance)

        return maxDistance
