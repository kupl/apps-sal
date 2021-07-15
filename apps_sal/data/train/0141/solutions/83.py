class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i,j = 0, len(people)-1
        c = 0
        while i <= j:
            if people[j] + people[i] <= limit:
                i += 1
            j -= 1
            c += 1
        return c
