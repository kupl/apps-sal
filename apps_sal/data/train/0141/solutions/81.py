class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        i = 0
        j = len(people) - 1
        while j >= i:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1
        return boats
