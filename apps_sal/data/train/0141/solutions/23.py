class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i = 0
        j = len(people) - 1
        total = 0
        while i <= j:
            if i == j:
                total += 1
                i += 1
                j -= 1
            else:
                if people[i] + people[j] <= limit:
                    i += 1
                    j -= 1
                    total += 1
                else:
                    j -= 1
                    total += 1
        return total
