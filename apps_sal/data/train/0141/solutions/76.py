class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        total = 0
        people.sort()
        i = 0
        j = len(people) - 1
        while i <= j:
            if people[i] + people[j] > limit or i == j:
                j -= 1
                total += 1
            else:
                i += 1
                j -= 1
                total += 1
        return total
