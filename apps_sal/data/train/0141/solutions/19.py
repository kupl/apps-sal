class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people = sorted(people)
        print(people)
        (i, j) = (0, len(people) - 1)
        while i <= j:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            boats += 1
        return boats
