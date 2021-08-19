class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) <= 1:
            return 0
        people.sort()
        boats = 0
        l = 0
        r = len(people) - 1
        while l <= r:
            if l == r:
                return boats + 1
            if people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            else:
                boats += 1
                r -= 1
        return boats
