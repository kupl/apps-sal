class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        res = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
        return i
