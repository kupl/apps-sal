class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        print(people)
        l = 0
        r = len(people) - 1
        boats = 0
        while l <= r:
            if people[r] + people[l] <= limit:
                r -= 1
                l += 1
                boats += 1
            else:
                r -= 1
                boats += 1
        return boats
