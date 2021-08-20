class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        (i, j) = (0, len(people) - 1)
        count = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                count += 1
                i += 1
                j -= 1
            else:
                count += 1
                j -= 1
        return count
