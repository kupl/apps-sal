class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sortedPeople = sorted(people)
        i = 0
        j = len(sortedPeople) - 1
        count = 0
        while i <= j:
            if i == j:
                count += 1
                i += 1
                j -= 1
                continue
            if sortedPeople[i] + sortedPeople[j] <= limit:
                count += 1
                i += 1
                j -= 1
            else:
                count += 1
                j -= 1

        return count
