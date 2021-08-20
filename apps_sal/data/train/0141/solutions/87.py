from collections import Counter


class Solution:

    def numRescueBoats(self, people, limit):
        people.sort(reverse=True)
        boats = 0
        r = len(people) - 1
        l = 0
        while l <= r:
            boats += 1
            if people[l] + people[r] <= limit:
                r -= 1
            l += 1
        return boats
