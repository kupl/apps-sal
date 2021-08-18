class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        boats = 0
        i = 0
        j = len(people) - 1

        while i <= j:
            boats += 1
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1

        return boats
