class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people = list(sorted(people, reverse=True))
        i = 0
        j = len(people) - 1
        while i <= j:
            if sorted_people[i] + sorted_people[j] <= limit:
                j -= 1
            i += 1
        return i
