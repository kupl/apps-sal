class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        total = 0
        while i <= j:
            total += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return total
