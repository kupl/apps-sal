class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        r = len(people) - 1
        l = 0
        trips = 0
        while r >= l:
            if people[r] + people[l] <= limit:
                l += 1
            trips += 1
            r -= 1
        return trips
