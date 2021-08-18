class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        nb_of_boats = 0
        i, j = 0, len(people) - 1

        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            nb_of_boats += 1

        return nb_of_boats
