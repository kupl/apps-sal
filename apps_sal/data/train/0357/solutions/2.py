class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left, right = [-1]*n, [-1]*n
        leftMost, rightMost = float('-inf'), float('inf')
        for i in range(n):
            if seats[i] == 1:   leftMost = i
            left[i] = leftMost
            if seats[n-1-i] == 1:   rightMost = n-1-i
            right[n-1-i] = rightMost
        print()
        maxDistance = 0
        for i in range(n):
            if seats[i] == 1:   continue
            distance = min(i-left[i], right[i]-i)
            maxDistance = max(maxDistance, distance)
        
        return maxDistance
