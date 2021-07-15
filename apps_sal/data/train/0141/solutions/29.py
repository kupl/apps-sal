from collections import deque
class Solution:
    def numRescueBoats(self, people, limit):
        n = len(people)
        weights = deque(sorted(people))
        boat = 0
        while n > 1:
            if weights[0] + weights[-1] <= limit:
                weights.popleft()
                weights.pop()
                n -= 2
            else:
                weights.pop()
                n -= 1
            boat += 1
        if n == 1: boat += 1
        return boat
