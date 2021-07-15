class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l = 0
        r = len(people) - 1
        while r>l:
            boats += 1
            if people[l] + people[r] <= limit:
                l += 1
                r = r-1
            else:
                r = r-1
        if r == l:
            boats += 1
        return boats
