class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        if len(seats) == 0 or min(seats) == 1:
            return 0

        left = [len(seats)] * len(seats)
        right = [len(seats)] * len(seats)
        latest = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                latest = i
            if latest >= 0:
                left[i] = i - latest

        latest = len(seats)
        for i in reversed(range(len(seats))):
            if seats[i] == 1:
                latest = i
            if latest < len(seats):
                right[i] = latest - i

        ans = 0
        for i in range(len(seats)):
            ans = max(ans, min(left[i], right[i]))

        print(left, right)

        return ans
